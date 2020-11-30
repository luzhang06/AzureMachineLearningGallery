# pylint: disable=E1136,W1202,R0913

""" Sequence embedding module"""

import sys
import argparse
from pathlib import Path
import joblib
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.utils.fileutils import ensure_folder
from azureml.studio.core.io.data_frame_directory \
     import load_data_frame_from_directory, save_data_frame_to_directory
from azureml.studio.core.io.model_directory import save_model_to_directory
from azureml.studio.core.data_frame_schema import DataFrameSchema
from sgt_module import compute_embeddings

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



def main(args=None):
    '''
      Module entry point function
    '''

    seq_col = args.sequence_column
    id_col = args.identifier_column
    length_sensitive = args.length_sensitive
    kappa = args.kappa

    logger.debug(f'input-dir {args.input_dir}')
    logger.debug(f'sequence-column {seq_col}')
    logger.debug(f'identifier-column {id_col}')
    logger.debug(f'length-sensitive {length_sensitive}')
    logger.debug(f'kappa {args.kappa}')
    logger.debug(f'output-dir {args.output_dir}')
    logger.debug(f'model output dir {args.model_output_dir}')

    input_df = load_data_frame_from_directory(args.input_dir).data

    if input_df[seq_col].isnull().sum().sum() > 0:
        logger.debug(f'column {seq_col} contains missing values ')
        sys.exit(1)

    embedding_df, sgt = compute_embeddings(input_df,
                                           seq_col,
                                           kappa,
                                           length_sensitive,
                                           id_col)

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
    PARSER.add_argument('--identifier-column', help="Sequence identifier column name")
    PARSER.add_argument('--length-sensitive', type=bool)
    PARSER.add_argument('--kappa', type=int)
    PARSER.add_argument('--delimiter', type=str)
    PARSER.add_argument('--output-dir', type=str,
                        help='dataframe containing embedding to output')
    PARSER.add_argument('--model-output-dir', type=str,
                        help="path to output directory to save model")

    ARGS, _ = PARSER.parse_known_args()
    main(ARGS)
