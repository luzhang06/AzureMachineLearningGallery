# pylint: disable=W1202
# pylint: disable=E1136

""" Sequence embedding module"""


import argparse
from pathlib import Path
import joblib
import pandas as pd
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.io.data_frame_directory \
     import load_data_frame_from_directory, save_data_frame_to_directory
from azureml.studio.core.io.model_directory import load_model_from_directory
from azureml.studio.core.data_frame_schema import DataFrameSchema

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

def score(input_df, sgt, seq_col, delimiter):

    '''
    Compute embeddings on score dataset using Sequence graph transform

    parameters:
        input_df: pandas dataframe input dataset
        sgt: SGT transformation state class
        seq_col: string, Column name containing the sequences to embedd

        delimiter:str,sequence delimiter default to none
                   for instance, a protein sequence the delimiter
                   can be ommited which will default to None
                   MEIEKTNRMNALFEFYAALLTDKQMNYIELYYADDYSLAEIAEEFGVSRQAVYDNIKRTEKILEDYEMKLHMY
                   another example where delimiter is ''~'' 1~2~3~3~3~3~3~3~1~4~5~1~2~3~3~3~3'
    return:
        scored embeddings pandas dataframe

    '''
    x_seq = input_df[seq_col]
    sequences = x_seq.str.split(delimiter).values

    embedding = sgt.transform(sequences)
    print('f embedding shape{embedding.shape}')

    output_df = pd.DataFrame(embedding, columns=[str(i) for i in range(embedding.shape[1])])
    return output_df



def main(args):
    '''
        Module entry point function
    '''
    seq_col = args.sequence_column
    delimiter = args.delimiter if args.delimiter is not None else None


    logger.debug(f'input-dir {args.input_dir}')
    logger.debug(f'model input dir {args.model_input_dir}')
    logger.debug(f'sequence-column {seq_col}')
    logger.debug(f'delimiter {delimiter}')
    logger.debug(f'output-dir {args.output_dir}')

    sgt = load_model_from_directory(args.model_input_dir, model_loader=joblib_loader).data
    input_df = load_data_frame_from_directory(args.input_dir).data

    embedding_df = score(input_df, sgt, seq_col, delimiter)
    print('f embedding shape{embedding_df.shape}')
    logger.debug(embedding_df.head())

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
    PARSER.add_argument('--delimiter', type=str, default=None,
                        help=f'sequence delimiter default to none \n'
                        f'for instance, a protein sequence the delimiter can be\
                        ommited which will default to None \n'
                        f'MEIEKTNRMNALFEFYAALLTDKQMNYIELYYADD     \n'
                        f'another example where delimiter is\
                         ''~'' 1~2~3~3~3~3~3~3~1~4~5~1~2~3~3~3~3')
    PARSER.add_argument('--output-dir', type=str, help="dataframe containing embedding to output")

    ARGS, _ = PARSER.parse_known_args()
    main(ARGS)
