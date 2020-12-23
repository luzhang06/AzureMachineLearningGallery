
"""Sequence graph transform module"""

import pandas as pd
from sgt import SGT

def score(input_df, sgt, seq_col, id_col=None):

    '''
    Compute embeddings on score dataset using Sequence graph transform

    parameters:
        input_df: pandas dataframe input dataset
        sgt: SGT transformation state class
        seq_col: string, Column name containing the sequences to embedd

    return:
        scored embeddings pandas dataframe

    '''
    corpus = pd.DataFrame(columns=(['id', 'sequence']))
    corpus['id'] = input_df.loc[:, id_col] if id_col is not None else input_df.index
    corpus['sequence'] = input_df.loc[:, seq_col].map(list)

    embedding_df = sgt.transform(corpus)
    print('f embedding shape{embedding_df.shape}')

    embedding_df.columns = embedding_df.columns.map(str)
    return embedding_df


def compute_embeddings(input_df, seq_col, kappa, length_sensitive, id_col=None):
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

    id_col:Sequence identifier colunmn name

    return:
     embeddings pandas dataframe
     sgt: transfromation state
    '''
    processing_mode = 'multiprocessing'
    corpus = pd.DataFrame(columns=(['id', 'sequence']))
    corpus['id'] = input_df.loc[:, id_col] if id_col is not None else input_df.index
    corpus['sequence'] = input_df.loc[:, seq_col].map(list)

    sgt = SGT(kappa=kappa,
              lengthsensitive=length_sensitive,
              mode=processing_mode)
    embedding_df = sgt.fit_transform(corpus)

    embedding_df.columns = embedding_df.columns.map(str)
    return embedding_df, sgt
