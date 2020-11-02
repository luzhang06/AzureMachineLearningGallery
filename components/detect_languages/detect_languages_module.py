# pylint: disable=R0903,W1202,R0801

"""Language detection module"""

import os
import argparse
import wget
import pandas as pd
import fasttext
from pycountry import languages
from azureml.studio.core.logger import module_logger as logger
from azureml.studio.core.io.data_frame_directory \
     import load_data_frame_from_directory, save_data_frame_to_directory
from azureml.studio.core.data_frame_schema import DataFrameSchema


class LanguagesDetector():
    ''' Language detection class '''

    def __init__(self):
        self.model_name = 'lid.176.bin'
        self.model_url = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin'
        if not os.path.exists(self.model_name):
            print(f'downloading {self.model_name} ...')
            wget.download(self.model_url, out=os.getcwd())

        self.model = fasttext.load_model(os.path.join(os.getcwd(), self.model_name))

    def detect_languages(self, input_df, cols):
        '''
        detect language in dataset
        args:
            input_df: Pandas Dataframe input dataset
            cols: list, list of text columns to run detection on

        return input_df with detection output appended
        '''

        def detect(text):
            pred = self.model.predict(text)
            iso_code = pred[0][0].replace('__label__', '')
            language_name = ''

            try:
                language_name = languages.get(alpha_2=iso_code).name
            except AttributeError:
                # language name lookup fail
                print(f'failed to query for language {pred}')
            return pd.Series([language_name, iso_code, round(pred[1][0], 2)],)

        for col_name in cols:
            input_df[col_name] = input_df[col_name].apply(lambda text: text.replace('\n', ' '))
            input_df[[f'{col_name}_language', f'{col_name}_ISO_639_code',\
                      f'{col_name}_likelihood']] = input_df[col_name].apply(detect)

        return input_df


def main(args=None):
    '''
        Module entry function
    '''


    logger.debug(f'input-dir {args.input_dir}')
    logger.debug(f'output-dir {args.output_dir}')

    input_df = load_data_frame_from_directory(args.input_dir).data
    columns_names = args.target_columns.split(',')

    lang_detector = LanguagesDetector()
    out_df = lang_detector.detect_languages(input_df, columns_names)
    logger.debug(f'output dataset {out_df.describe()}')

    save_data_frame_to_directory(save_to=args.output_dir,
                                 data=out_df,
                                 schema=DataFrameSchema.data_frame_to_dict(out_df))

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser()

    PARSER.add_argument('--input-dir', help='Dataset to train')
    PARSER.add_argument('--target-columns', type=str, help='target column')
    PARSER.add_argument('--output-dir', type=str, help='dataframe containing detected langauges')

    ARGS, _ = PARSER.parse_known_args()
    main(ARGS)
