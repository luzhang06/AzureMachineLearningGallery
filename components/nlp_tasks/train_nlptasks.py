# pylint: disable=R0801
""" Text classification Module entry point"""

from pathlib import Path
import joblib
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.utils.fileutils import ensure_folder
from azureml.studio.core.io.data_frame_directory\
             import load_data_frame_from_directory, save_data_frame_to_directory
from azureml.studio.core.io.model_directory import  save_model_to_directory
from azureml.studio.core.data_frame_schema import DataFrameSchema
from args import module_args_parser
from tasks import TextClassificationTask


# extract https://github.com/hirofumi-s-friends/recommenders
def nlptasks_module_dumper(data, file_name=None):
    '''
    Return a dumper to dump a model with pickle.
    args:
        data: transformer instance to serialize
        filername:str file name to write to

    '''
    if not file_name:
        file_name = '_nlptasks.pkl'

    def nlp_model_dumper(save_to):
        full_path = Path(save_to) / file_name
        ensure_folder(Path(save_to))
        with open(full_path, 'wb') as fout:
            joblib.dump(data, fout, protocol=4)

        return {'model_type': 'joblib', 'file_name': file_name}


    return nlp_model_dumper

def main(args):
    ''' module entry point'''

    supported_tasks = {'classification':TextClassificationTask}

    model_args = {'manual_seed':args.seed,
                  'n_gpu':args.n_gpu,
                  'max_seq_length':args.max_seq_length,
                  'num_train_epochs':args.num_train_epochs,
                  'train_batch_size':args.train_batch_size,
                  'eval_batch_size':args.eval_batch_size,
                  'learning_rate':args.learning_rate,
                  'epsilon_adam':args.epsilon_adam,
                  'warmup_steps':args.warmup_steps,
                  'warmup_ratio':args.warmup_ratio,
                  'weight_decay':args.weight_decay,
                  'gradient_accumulation_steps':args.gradient_accumulation_steps,
                  'max_grad_norm':args.max_grad_norm,
                  'do_lower_case':args.do_lower_case,
                  'fp16':False,
                  'overwrite_output_dir':True,
                  'tensorboard_dir': args.tb_logs,
                  'output_dir':args.model_output_dir,
                  'regression':True if args.task=='regression' else False
                 }

    model_type = args.model_type
    model_name = vars(args)[f'{model_type}_model_name']
    if args.task in ['binary_classification', 'multi-class_classification', 'regression']:
        nlptask = supported_tasks['classification'](model_type,
                                                    model_name,
                                                    args.task,
                                                    model_args
                                                   )

    logger.debug('==============================================================='
                 '==============================================================='
                 '===============================================================')
    logger.debug(nlptask.model_args)


    train_df = load_data_frame_from_directory(args.train_dir).data
    eval_df = load_data_frame_from_directory(args.eval_dir).data

    result_df, metrics_df = nlptask.train(train_df,
                                          eval_df,
                                          args.text_column,
                                          args.label_column)

    logger.debug('================================================================'
                 '================================================================'
                 '================================================================')
    logger.debug(nlptask.model.model)

    save_data_frame_to_directory(save_to=args.output_dir,
                                 data=result_df,
                                 schema=DataFrameSchema.data_frame_to_dict(result_df))

    save_data_frame_to_directory(save_to=args.metrics_output_dir,
                                 data=metrics_df,
                                 schema=DataFrameSchema.data_frame_to_dict(metrics_df))

    save_model_to_directory(save_to=args.model_output_dir,
                            model_dumper=nlptasks_module_dumper(data=nlptask))


if __name__ == '__main__':
    ARGS, _ = module_args_parser().parse_known_args()
    main(ARGS)
