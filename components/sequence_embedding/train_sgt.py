# pylint: disable=E1136
# pylint: disable=W1202

""" Sequence embedding module"""


import argparse
from distutils.util import strtobool
from pathlib import Path
import joblib
import pandas as pd
from sgt import Sgt
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.utils.fileutils import ensure_folder
from azureml.studio.core.io.data_frame_directory \
     import load_data_frame_from_directory, save_data_frame_to_directory
from azureml.studio.core.io.model_directory import save_model_to_directory
from azureml.studio.core.data_frame_schema import DataFrameSchema

# extract https://github.com/hirofumi-s-friends/recommenders
def sgt_dumper(data, file_name=None):
    """Return a dumper to dump a model with pickle."""
    if not file_name:
        file_name = '_sgt.pkl'

    def sgt_model_dumper(save_to):
        full_path = Path(save_to) / file_name
        ensure_folder(Path(save_to))
        with open(full_path, 'wb') as fout:
            joblib.dump(data, fout, protocol=4)

        sgt_model_spec = {'model_type': 'joblib', 'file_name': file_name}
        return sgt_model_spec

    return sgt_model_dumper

def compute_embeddings(input_df, seq_col, delimiter, kappa, length_sensitive):
    '''
    Compute embeddings using Sequence graph transform

    parameters:
     input_df: pandas dataframe input dataset

    seq_col: string, Column name containing the sequences to embed
    length-sensitive:bool, This is set to true if the embedding of
                           should have the information of the length of the sequence.
                           If set to false then the embedding of two sequences with
                           similar pattern but different lengths will be the same.

    kappa':int, Hyper parameter, kappa > 0, to change the extraction of
                 long-term dependency. Higher the value the lesser
                 the long-term dependency captured in the embedding.
                 Typical values for kappa are 1, 5, 10.

    delimiter:str,sequence delimiter default to none
                   for instance, a protein sequence the delimiter
                   can be ommited which will default to None
                   MEIEKTNRMNALFEFYAALLTDKQMNYIELYYADDYSLAE
                   another example where delimiter is ''~'' 1~2~3~3~3~3~3~3~1~4~5~1~2~3~3~3~3'
    return:
     embeddings pandas dataframe
     sgt: transfromation state
    '''
    x_seq = input_df[seq_col]
    sequences = x_seq.str.split(delimiter).values

    sgt = Sgt(kappa=kappa, lengthsensitive=length_sensitive)
    embedding = sgt.fit_transform(sequences)

    embedding_df = pd.DataFrame(embedding, columns=[str(i) for i in range(embedding.shape[1])])

    return embedding_df, sgt

def main(args=None):
    '''
      Module entry point function
    '''

    seq_col = args.sequence_column
    length_sensitive = strtobool(args.length_sensitive)
    delimiter = args.delimiter if args.delimiter is not None else None


    logger.debug(f'input-dir {args.input_dir}')
    logger.debug(f'sequence-column {seq_col}')
    logger.debug(f'length-sensitive {length_sensitive}')
    logger.debug(f'kappa {args.kappa}')
    logger.debug(f'delimiter {delimiter}')
    logger.debug(f'output-dir {args.output_dir}')
    logger.debug(f'model output dir {args.model_output_dir}')

    input_df = load_data_frame_from_directory(args.input_dir).data
    embedding_df, sgt = compute_embeddings(input_df, seq_col, delimiter,
                                           args.kappa, length_sensitive)

    logger.debug(f'embedding shape {embedding_df.shape}')

    save_data_frame_to_directory(save_to=args.output_dir,
                                 data=embedding_df,
                                 schema=DataFrameSchema.data_frame_to_dict(embedding_df))


    save_model_to_directory(save_to=args.model_output_dir,
                            model_dumper=sgt_dumper(data=sgt))



if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()

    PARSER.add_argument('--input-dir', help='Dataset to train')
    PARSER.add_argument('--sequence-column', type=str)
    PARSER.add_argument('--length-sensitive', type=str)
    PARSER.add_argument('--kappa', type=int)
    PARSER.add_argument('--delimiter', type=str)
    PARSER.add_argument('--output-dir', type=str,
                        help='dataframe containing embedding to output')
    PARSER.add_argument('--model-output-dir', type=str,
                        help="path to output directory to save model")

    ARGS, _ = PARSER.parse_known_args()
    main(ARGS)
