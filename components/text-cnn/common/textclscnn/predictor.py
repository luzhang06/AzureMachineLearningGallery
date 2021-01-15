import os
import pickle
from inspect import signature

import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from sklearn.metrics import (average_precision_score, f1_score,
                             precision_recall_curve, precision_score,
                             recall_score)
from torch.autograd import Variable

from azureml.core.run import Run
from textclscnn.utils.args_util import predict_args
from textclscnn.common.model import TextCNN
import logging


class Predictor():
    def __init__(self, model_folder):
        self.model_path = model_folder
        # config file must be loaded to init a model
        with open(os.path.join(self.model_path, 'config.pkl'), 'rb') as f:
            config = pickle.load(f)
        self.config = config
        self.label_column = config.label_column
        self.model = TextCNN(config)
        # model weight file must be loaded to get learnt weight.
        model_file = os.path.join(model_folder, "best_model.pt")
        if model_file is not None:
            self.model.load_state_dict(torch.load(model_file))
        else:
            raise FileNotFoundError("Model File Not Exist")
        # user may set device id here, but now let us ignore it.
        if torch.cuda.is_available() and config.cuda:
            self.model = self.model.cuda()
        self.model.eval()

    def predict(self, data_frame):
        output_label = []
        output_prob = []
        with torch.no_grad():
            for index, row in data_frame.iterrows():
                input_setence = row['text_id']
                x = Variable(torch.LongTensor([input_setence]))
                if torch.cuda.is_available() and self.config.cuda:
                    x = x.cuda()
                output = self.model(x)
                softmax = nn.Softmax(dim=1)
                pred_probs = softmax(output).cpu().numpy()[0]
                index = torch.argmax(output, 1)[0].cpu().item()
                output_label.append(index)
                # use positive category prob as scored prob for metric pr curve.
                output_prob.append(pred_probs[index] if index == 1 else 1 - pred_probs[index])
            data_frame['Scored Label'] = output_label
            data_frame['Scored Prob'] = output_prob
        data_frame.drop(['text_id'], axis=1, inplace=True)
        return data_frame

    def prcurve(self, df_true, df_predict, df_prob):
        average_precision = average_precision_score(df_true, df_predict)
        precision, recall, _ = precision_recall_curve(df_true, df_prob)
        step_kwargs = ({
            'step': 'post'
        } if 'step' in signature(plt.fill_between).parameters else {})
        f1_plt = plt.figure(1)
        plt.step(recall, precision, color='b', alpha=0.2, where='post')
        plt.fill_between(recall,
                         precision,
                         alpha=0.2,
                         color='b',
                         **step_kwargs)
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.ylim([0, 1.1])
        plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
            average_precision))

        return f1_plt

    def scores(self, df_true, df_predict):
        f2_plt = plt.figure(2)
        metrics_name = ['Precision', 'Recall', 'F1-Score']
        logging.info(f'true label value counts: {df_true.value_counts()}')
        logging.info(f'pred label value counts: {df_predict.value_counts()}')
        p = precision_score(df_true, df_predict, average='binary')
        r = recall_score(df_true, df_predict, average='binary')
        f1 = f1_score(df_true, df_predict, average='binary')
        logging.info(f'p {p}, r {r}, f1 {f1}')
        values_list = [p, r, f1]
        plt.bar(metrics_name,
                values_list,
                width=0.8,
                facecolor="#ff9999",
                edgecolor="white")

        for x, y in zip(metrics_name, values_list):
            plt.text(x, y, '%.4f' % y, ha='center', va='bottom')
        plt.ylim([0, 1.1])
        plt.ylabel('score')
        plt.title('Scores')

        return f2_plt

    def evaluation(self, train_config, test_data, predict_result, output_eval_dir):
        label_column = train_config.label_column
        logging.info(f'label column {label_column}')
        
        if label_column in test_data.columns:
            logging.info(f"Got actual label column {label_column}, evaluating:")
            true_labels = test_data[label_column]

            if train_config.true_label_value:
                true_labels = true_labels.apply(lambda x: 1 if x == train_config.true_label_value else 0)

            scored_labels = predict_result['Scored Label']
            scored_probs = predict_result['Scored Prob']

            run = Run.get_context()

            f1_plt = self.prcurve(true_labels, scored_labels, scored_probs)
            run.log_image("precision-recall curve", plot=f1_plt)
            f1_plt.savefig(os.path.join(output_eval_dir, 'precision_recall.png'))

            f2_plt = self.scores(true_labels, scored_labels)
            run.log_image("scores", plot=f2_plt)
            f2_plt.savefig(os.path.join(output_eval_dir, 'scores.png'))



