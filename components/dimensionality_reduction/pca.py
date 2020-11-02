# pylint: disable=E1136,W1202,R0801

""" Dimensionality reduction entry module"""

from pathlib import Path
import joblib
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.utils.fileutils import ensure_folder
from azureml.studio.core.io.data_frame_directory\
             import load_data_frame_from_directory, save_data_frame_to_directory
from azureml.studio.core.io.model_directory import  save_model_to_directory
from azureml.studio.core.data_frame_schema import DataFrameSchema
from pca_module import PCAModule
from module_parser import pca_parser


# extract https://github.com/hirofumi-s-friends/recommenders
def pca_module_dumper(data, file_name=None):
    '''
    Return a dumper to dump a model with pickle.
    args:
        data: transformer instance to serialize
        filername:str file name to write to

    '''
    if not file_name:
        file_name = '_pca.pkl'

    def model_dumper(save_to):
        full_path = Path(save_to) / file_name
        ensure_folder(Path(save_to))
        with open(full_path, 'wb') as fout:
            joblib.dump(data, fout, protocol=4)

        model_spec = {'model_type': 'joblib', 'file_name': file_name}
        return model_spec

    return model_dumper


def main(args):

    '''
    Module entry function

    args:
      args:list transformer parameters requested by user/

   '''

    logger.debug(f'input-dir {args.input_dir}')
    logger.debug(f'output-dir {args.output_dir}')
    logger.debug(f'model output dir {args.model_output_dir}')

    input_df = load_data_frame_from_directory(args.input_dir).data
    logger.debug(f'{input_df.describe()}\n shape{input_df.shape} ')

    pca_module = PCAModule(args)
    logger.debug(pca_module.pca_instance)

    output_df = pca_module.fit_transform(input_df)
    pca_module.log_metrics(input_df.columns)

    logger.debug(f'output shape {output_df.shape}')
    save_data_frame_to_directory(save_to=args.output_dir,
                                 data=output_df,
                                 schema=DataFrameSchema.data_frame_to_dict(output_df))

    save_model_to_directory(save_to=args.model_output_dir,
                            model_dumper=pca_module_dumper(data=pca_module))




if __name__ == '__main__':
    ARGS, _ = pca_parser().parse_known_args()
    main(ARGS)
