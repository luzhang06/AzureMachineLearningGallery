import pickle
import re

import nltk
import pandas as pd
from nltk.tokenize import word_tokenize

from textclscnn.utils.args_util import preprocess_args
import logging


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


class DataPreprocessor(object):
    def __init__(self, vocab_path, text_column):
        self.vocab_path = vocab_path
        self.text_column = text_column
        self.rule = re.compile(r"[^\u4e00-\u9fa5]")
        self.cut = word_tokenize
        with open(self.vocab_path + '/' + 'word2id.pkl', 'rb') as f:
            self.word2id = pickle.load(f)

    def process(self, data_frame: pd.DataFrame):
        out_df = data_frame.copy()
        out_df['text_id'] = data_frame[self.text_column].apply(lambda text: [
            self.word2id[word] if word != '\x00' and word in self.word2id else
            0 for word in word_tokenize(text)
        ])
        logging.info(f'first 5 lines of processed df: {out_df.head()}')
        return out_df

