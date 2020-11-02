# pylint: disable=R0903,W0221,W0201,C0301,E1101,E1102,R0902

""" NLP tasks module """


from abc import ABC, abstractmethod

import logging
import numpy as np
import pandas as pd

import torch
import torch.nn.functional as F

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (accuracy_score,
                             f1_score,
                             recall_score,
                             precision_score,
                             mean_absolute_error,
                             mean_squared_error,
                             r2_score
                            )

from simpletransformers.classification import ClassificationModel




PRETRAINED_MODELS_CLASSIFICATION = {
        'bert':[
            'bert-base-uncased',
            'bert-large-uncased',
            'bert-base-cased',
            'bert-large-cased',
            'bert-base-multilingual-uncased',
            'bert-base-multilingual-cased',
            'bert-base-chinese',
            'bert-base-german-cased',
            'bert-large-uncased-whole-word-masking',
            'bert-large-cased-whole-word-masking',
            'bert-large-uncased-whole-word-masking-finetuned-squad',
            'bert-large-cased-whole-word-masking-finetuned-squad',
            'bert-base-german-dbmdz-cased',
            'bert-base-german-dbmdz-uncased',
            'bert-base-finnish-cased-v1',
            'bert-base-finnish-uncased-v1',
            'bert-base-dutch-cased'],
        'xlnet':[
            'xlnet-base-cased',
            'xlnet-large-cased'],
        'xlm':[
            'xlm-mlm-en-2048',
            'xlm-mlm-ende-1024',
            'xlm-mlm-enfr-1024',
            'xlm-mlm-enro-1024',
            'xlm-mlm-xnli15-1024'],
        'roberta':[
            'roberta-base',
            'roberta-large',
            'distilroberta-base'],
        'distilbert':[
            'distilbert-base-uncased',
            'distilbert-base-uncased-distilled-squad',
            'distilbert-base-cased',
            'distilbert-base-cased-distilled-squad',
            'distilbert-base-german-cased',
            'distilbert-base-multilingual-cased'],
        'albert':[
            'albert-base-v1',
            'albert-large-v1',
            'albert-base-v2',
            'albert-large-v2'],
        'camembert':[
            'camembert-base'],
        'xlmroberta':[
            'xlm-roberta-base',
            'xlm-roberta-large'],
        'flaubert':[
            'flaubert-small-cased',
            'flaubert-base-uncased',
            'flaubert-base-cased',
            'flaubert-large-cased'],
        'electra':[
            'google/electra-base-discriminator',
            'google/electra-small-discriminator',
            'google/electra-large-discriminator']
        }

def f1_score_micro(y_true, y_pred):
    ''' F1 micro'''
    return f1_score(y_true, y_pred, average="micro")

def f1_score_macro(y_true, y_pred):
    ''' F1 macro'''
    return f1_score(y_true, y_pred, average="macro")

def recall_score_micro(y_true, y_pred):
    ''' Recall micro'''
    return recall_score(y_true, y_pred, average="micro")

def recall_score_macro(y_true, y_pred):
    ''' Recall macro'''
    return recall_score(y_true, y_pred, average="macro")

def precision_score_micro(y_true, y_pred):
    ''' Precision micro'''
    return precision_score(y_true, y_pred, average="micro")

def precision_score_macro(y_true, y_pred):
    ''' Precision macro'''
    return precision_score(y_true, y_pred, average="macro")

MULTI_CLASS_EVAL_METRICS = {
    "Overall_accuracy": accuracy_score,
    "Micro_Recall": recall_score_micro,
    "Macro_Recall": recall_score_macro,
    "Micro_Precision": precision_score_micro,
    "Macro_Precision": precision_score_macro,
    "F1_Micro": f1_score_micro,
    "F1_Macro": f1_score_macro
    }

BINARY_CLASS_EVAL_METRICS = {
    "Accuracy":accuracy_score,
    "Recall":recall_score,
    "Precision":precision_score,
    "F1":f1_score
    }

REGRESSION_EVAL_METRICS = {
    'MAE': mean_absolute_error,
    'MSE': mean_squared_error,
    'R2': r2_score
}

class Task(ABC):
    '''interface for nlp tasks'''

    @abstractmethod
    def train(self, train_df, eval_df, **kwargs):
        ''' Pipeline invocation base train method'''
        raise NotImplementedError()

    @abstractmethod
    def predict(self, pred_df):
        ''' Pipeline invocation base predict method'''
        raise NotImplementedError()

class TextClassificationTask(Task):

    '''
        Text Classification task class

       Support Binary & multiclass classification and Regression tasks
    '''

    def __init__(self, #pylint:disable=R0913
                 model_type,
                 model_name,
                 task,
                 model_args):

        assert model_type in PRETRAINED_MODELS_CLASSIFICATION.keys()
        assert model_name in PRETRAINED_MODELS_CLASSIFICATION[model_type]

        logging.basicConfig(level=logging.INFO)
        self.transformers_logger = logging.getLogger("transformers")
        self.transformers_logger.setLevel(logging.WARNING)

        self.task = task
        self.model_type = model_type
        self.model_name = model_name
        self.model_args = model_args
        self.label_encoder = LabelEncoder()

    def train(self,
              train_df,
              eval_df,
              text_column,
              label_column):

        '''
         Train & eval classificationModel
         Args:
            train_df: Pandas dataframe containing training dataset
            eval_df: Pandas  dataframecontaining evaluation dataset
            text_column: string name of corpora column
            label_column: string name of label column

        return:
             prediction_df pandas dataframe with eval_df appended with prediction
             model_output_df: pandas dataframe  metric outputs from evaluation
        '''

        text_col = 'text'
        label_col = 'labels'

        train_df = train_df.rename({text_column:text_col}, axis=1)
        eval_df = eval_df.rename({text_column:text_col}, axis=1)

        if self.task in ['binary_classification', 'multi-class_classification']:
            train_df[label_col] = self.label_encoder.fit_transform(train_df[label_column].values)
            eval_df[label_col] = self.label_encoder.fit_transform(eval_df[label_column].values)

        if self.task == 'regression':
            self.num_labels = 1
        else:
            self.num_labels = train_df[label_col].nunique()

        self.model = ClassificationModel(self.model_type,
                                         self.model_name,
                                         args=self.model_args,
                                         num_labels=self.num_labels,
                                         use_cuda=True)

        self.model.train_model(train_df)
        prediction_df, metrics_df = self.__evaluate(eval_df, text_column, label_column)
        return prediction_df, metrics_df


    def __evaluate(self, eval_df, text_column, label_column):
        '''
           Evaluate the model on eval_df

           Meant to be private and called within train method

           Args:
                eval_df: Pandas dataframe evaluation dataset
                text_column: user text column

           return:
                prediction_df: Pandas dataframe containing scored labels
                            appended to text column
                metrics_df: Pandas dataframe containing metrics
                        computed on evaluation dataset
        '''

        metrics = MULTI_CLASS_EVAL_METRICS    #default to multi-class
        if self.task == 'regression':
            metrics = REGRESSION_EVAL_METRICS
        elif self.task == 'binary_classification':
            metrics = BINARY_CLASS_EVAL_METRICS

        result, model_outputs, _ = self.model.eval_model(eval_df, **metrics)
        metrics_df = pd.DataFrame.from_dict([result])

        if self.task in ['binary_classification', 'multi-class_classification']:
            metrics_df.drop(['mcc'], axis=1, inplace=True)
            prediction_df = pd.DataFrame(F.softmax(torch.tensor(model_outputs), dim=1).cpu().detach().numpy(),
                                         columns=[f'Scored_Probabilities_{col}'
                                                  for col in self.label_encoder.inverse_transform(range(self.num_labels))
                                                 ]
                                         )
        else:   #regression
            prediction_df = pd.DataFrame(model_outputs, columns=['scored_labels'])

        prediction_df.insert(0, text_column, eval_df.text.values)
        prediction_df.insert(1, label_column, eval_df[label_column].values)

        return prediction_df, metrics_df


    def predict(self, pred_df):
        '''

        Predict on pred_df using trained model

        Args:
            pred_df: Pandas data frame containing text on which to generate prediction

        return:
            result_df: Pandas dataframe return Scored labels
            raw_df: Pandas dataframe containing probabilities for  all labels
                    For regression task raw_df is None

        '''

        input_shape = pred_df.values.shape
        input_arr = np.concatenate(pred_df.values.reshape(input_shape[0], 1))

        pred, raw = self.model.predict(input_arr)

        raw_df = None

        if self.task in ['binary_classification', 'multi-class_classification']:
            result_df = pd.DataFrame(self.label_encoder.inverse_transform(pred),
                                     columns=['Scored_labels'])

            raw_df = pd.DataFrame(F.softmax(torch.tensor(raw), dim=1).cpu().detach().numpy(),
                                  columns=[f'Scored_Probabilities_{col}'
                                           for col in self.label_encoder.inverse_transform(range(self.num_labels))]
                                 )
        else:        #regression
            result_df = pd.DataFrame(pred.ravel(), columns=['scored_labels'])

        result_df.insert(0, pred_df.name, pred_df.values)

        return result_df, raw_df
