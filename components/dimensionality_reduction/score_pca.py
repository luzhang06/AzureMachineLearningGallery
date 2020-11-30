# pylint: disable=W1202

"""Score dimensionality reduction module """
import argparse
from pathlib import Path
import joblib
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.io.data_frame_directory\
             import load_data_frame_from_directory, save_data_frame_to_directory
from azureml.studio.core.io.model_directory import  load_model_from_directory
from azureml.studio.core.data_frame_schema import DataFrameSchema



def pcamodule_loader(load_from_dir, model_spec):
    '''
        load transformation state from disc
        args:
            load_from_dir, string, path to file
            model_spec: dict aml artifacts
        return transformation object
    '''
    file_name = model_spec['file_name']
    with open(Path(load_from_dir) / file_name, 'rb') as fin:
        return joblib.load(fin)

def score(module, input_df):
    '''
        Transform dataset on previously fitted pcamodule
        Args:
            module: PCAModule fitted during training
            input_df: Pandas dataframe
        return pandas dataframe principal components
    '''

    return module.transform(input_df)

def main(args):

    '''
    Module entry function

    args:
      args:list, user parameters

   '''

    logger.debug(f'input-dir {args.input_dir}')
    logger.debug(f'model input dir {args.model_input_dir}')

    logger.debug(f'output-dir {args.output_dir}')

    input_df = load_data_frame_from_directory(args.input_dir).data
    logger.debug(f'{input_df.describe()}\n shape{input_df.shape} ')

    pca_module = load_model_from_directory(args.model_input_dir,
                                           model_loader=pcamodule_loader).data

    logger.debug(pca_module.pca_instance)

    output_df = score(pca_module, input_df)

    logger.debug(f'output shape {output_df.shape}')
    save_data_frame_to_directory(save_to=args.output_dir,
                                 data=output_df,
                                 schema=DataFrameSchema.data_frame_to_dict(output_df))




if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('--input-dir', help='Dataset to score')
    PARSER.add_argument('--model-input-dir', type=str,
                        help="path to model input directory")
    PARSER.add_argument('--output-dir', type=str, help="Output Dataframe")

    ARGS, _ = PARSER.parse_known_args()
    main(ARGS)
