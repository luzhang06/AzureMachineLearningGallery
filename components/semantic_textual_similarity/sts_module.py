# pylint: disable=W1202,R0913


""" Semantic textual similarity module entry"""

import sys
import argparse
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.io.data_frame_directory \
     import load_data_frame_from_directory, save_data_frame_to_directory
from azureml.studio.core.data_frame_schema import DataFrameSchema
from sts import TextualSimilarity



SUPPORTED_TRANSFORMERS = {'bert-base':'bert-base-nli-stsb-mean-tokens',
                          'bert-large':'bert-large-nli-stsb-mean-tokens',
                          'roberta-base':'roberta-base-nli-stsb-mean-tokens',
                          'roberta-large':'roberta-large-nli-stsb-mean-tokens',
                          'distilbert-base':'distilbert-base-nli-stsb-mean-tokens'}


def main(args):

    '''
        Module entry function
    '''

    transformer = SUPPORTED_TRANSFORMERS[args.transformer]

    logger.debug(f'input-dir {args.input_dir}')
    logger.debug(f'column {args.column_name}')
    logger.debug(f'distance {args.distance}')
    logger.debug(f'transformer {transformer}')
    logger.debug(f'sim-dir {args.sim_dir}')

    input_df = load_data_frame_from_directory(args.input_dir).data

    if input_df[args.column_name].isnull().sum().sum() > 0:
        logger.debug(f'column{args.column_name} contains missing values ')
        sys.exit(1)

    sts = TextualSimilarity(transformer=transformer, distance_func=args.distance)
    embedding_df, sim_df = sts.fit_transform(input_df[args.column_name].values)

    sim_df.insert(0, args.column_name, input_df[args.column_name])

    logger.debug(f'similarity matrix shape {sim_df.shape}')
    logger.debug(f'embedding  shape {embedding_df.shape}')

    save_data_frame_to_directory(save_to=args.sim_dir,
                                 data=sim_df,
                                 schema=DataFrameSchema.data_frame_to_dict(sim_df))

    save_data_frame_to_directory(save_to=args.embedding_dir,
                                 data=embedding_df,
                                 schema=DataFrameSchema.data_frame_to_dict(embedding_df))


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()

    PARSER.add_argument('--input-dir', help='Dataset to train')
    PARSER.add_argument('--transformer', type=str, help='Prentrained sentence bert')
    PARSER.add_argument('--column-name', type=str, help='colunmn name containing corpus')
    PARSER.add_argument('--distance', type=str, help='distance function')
    PARSER.add_argument('--sim-dir', type=str, help='dataframe containing similarity matrix')
    PARSER.add_argument('--embedding-dir', type=str, help='dataframe containing embedding')

    ARGS, _ = PARSER.parse_known_args()
    main(ARGS)
