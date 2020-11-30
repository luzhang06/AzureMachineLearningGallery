# pylint: disable=W1202,E1136

""" Sequence embedding module"""


import sys
import argparse
from pathlib import Path
import joblib
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.io.data_frame_directory \
     import load_data_frame_from_directory, save_data_frame_to_directory
from azureml.studio.core.io.model_directory import load_model_from_directory
from azureml.studio.core.data_frame_schema import DataFrameSchema
from sgt_module import score

def joblib_loader(load_from_dir, model_spec):
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



def main(args):
    '''
        Module entry point function
    '''



    seq_col = args.sequence_column
    id_col = args.identifier_column

    logger.debug(f'input-dir {args.input_dir}')
    logger.debug(f'model input dir {args.model_input_dir}')
    logger.debug(f'sequence-column {seq_col}')
    logger.debug(f'identifier-column {id_col}')
    logger.debug(f'output-dir {args.output_dir}')

    sgt = load_model_from_directory(args.model_input_dir, model_loader=joblib_loader).data
    input_df = load_data_frame_from_directory(args.input_dir).data

    if input_df[seq_col].isnull().sum().sum() > 0:
        print(f'column{seq_col} contains missing values ')
        sys.exit(1)

    embedding_df = score(input_df, sgt, seq_col, id_col)
    print('f embedding shape{embedding_df.shape}')
    print(embedding_df.head())

    save_data_frame_to_directory(save_to=args.output_dir,
                                 data=embedding_df,
                                 schema=DataFrameSchema.data_frame_to_dict(embedding_df))



if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('--input-dir', help='Dataset to score')
    PARSER.add_argument('--model-input-dir', type=str,
                        help="path to model input directory")
    PARSER.add_argument('--sequence-column', type=str,
                        help='Column name containing the sequences to embedd')
    PARSER.add_argument('--identifier-column', help="Sequence identifier column name")
    PARSER.add_argument('--output-dir', type=str, help="dataframe containing embedding to output")

    ARGS, _ = PARSER.parse_known_args()
    main(ARGS)
