# pylint: disable=W1202

"""Score NLP tasks module """


from pathlib import Path
import joblib
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.io.data_frame_directory\
             import load_data_frame_from_directory, save_data_frame_to_directory
from azureml.studio.core.io.model_directory import  load_model_from_directory
from azureml.studio.core.data_frame_schema import DataFrameSchema
from args import score_arg_parser

# extract https://github.com/hirofumi-s-friends/recommenders
def nlptasks_module_loader(load_from_dir, model_spec):
    '''
        load trained model
        args:
            load_from_dir, string, path to file
            model_spec: dict aml artifacts
        return trained model
    '''
    file_name = model_spec['file_name'] #_nlptasks.pkl
    with open(Path(load_from_dir) / file_name, 'rb') as fin:
        return joblib.load(fin)


def main(args):

    '''
    Module entry function

    args:
      args:list, user parameters

   '''

    input_df = load_data_frame_from_directory(args.input_dir).data
    logger.debug(f'Input shape {input_df.shape}')

    nlptasks_clf = load_model_from_directory(args.model_input_dir,
                                             model_loader=nlptasks_module_loader).data

    logger.debug(input_df[args.text_column])
    output_df, _ = nlptasks_clf.predict(input_df[args.text_column])

    logger.debug(f'Output shape {output_df.shape}')
    save_data_frame_to_directory(save_to=args.output_dir,
                                 data=output_df,
                                 schema=DataFrameSchema.data_frame_to_dict(output_df))



if __name__ == '__main__':

    ARGS, _ = score_arg_parser().parse_known_args()
    main(ARGS)
