# pylint: disable=R0903
# pylint: disable=W1202

"""Compute correlation module"""

import argparse
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.io.data_frame_directory \
     import load_data_frame_from_directory, save_data_frame_to_directory
from azureml.studio.core.data_frame_schema import DataFrameSchema

class ComputeCorrelationModule():
    """Compute correlation class module"""
    def __init__(self, corr_type):
        self._supported_corr_types = ['kendall', 'pearson', 'spearman']
        assert corr_type in self._supported_corr_types
        self.corr_type = corr_type

    def compute(self, input_df):
        '''
        Compute correlation matrix based on correlation type provided in constructor

        parameters:
           df: Pandas dataframe of shape (m,n), expects numeric values.
               Columns with other types than numeric will be ignored.
               Columns with NaN will be return as NaN

        return correlation matrix as pandas dataframe of shape (n,n)
        '''
        logger.debug(f'datatypes found {input_df.dtypes}')
        logger.debug(f'probe dataset {input_df.describe()}')
        return input_df.corr(self.corr_type)

def main(args=None):
    '''
        Module entry function
    '''
    input_dir = args.input_dir
    corr_type = args.correlation_method

    logger.debug(f'input-dir {input_dir}')
    logger.debug(f'correlation-method {corr_type}')
    logger.debug(f'output-dir {args.output_dir}')
    input_df = load_data_frame_from_directory(args.input_dir).data

    corr_df = ComputeCorrelationModule(corr_type).compute(input_df)
    logger.debug(f'correlation matrix shape {corr_df.shape}')

    save_data_frame_to_directory(save_to=args.output_dir,
                                 data=corr_df,
                                 schema=DataFrameSchema.data_frame_to_dict(corr_df))


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()

    PARSER.add_argument('--input-dir', help='Dataset to train')
    PARSER.add_argument('--correlation-method', type=str, help='correlation method')
    PARSER.add_argument('--output-dir', type=str,
                        help='dataframe containing correlation matrix to output')

    ARGS, _ = PARSER.parse_known_args()
    main(ARGS)
