# pylint: disable=W1202
# pylint: disable=R0903

"""Semantic textual similarity module"""


import pandas as  pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances

class TextualSimilarity():

    '''Semantic textual similarity class'''

    def __init__(self, transformer, distance_func):
        self.supported_sentence_transformers = ['bert-base-nli-stsb-mean-tokens',
                                                'bert-large-nli-stsb-mean-tokens',
                                                'roberta-base-nli-stsb-mean-tokens',
                                                'roberta-large-nli-stsb-mean-tokens',
                                                'distilbert-base-nli-stsb-mean-tokens']

        self.supported_distances = {'cosine':cosine_similarity, 'euclidean':euclidean_distances, \
                                    'manhattan':manhattan_distances}

        assert transformer in self.supported_sentence_transformers
        assert distance_func in [*self.supported_distances.keys()]


        self.requested_distance_func = distance_func
        self.requested_transformer = transformer

        print(f'distance {self.requested_distance_func }')
        print(f'transformer {self.requested_transformer}')


    def fit_transform(self, corpus):
        '''
        return module outcome similarity matrix and embeddings

        args:
            corpus: list of sentences of size n

        return:
            similarity matrix: pandas dataframe
            sentence embedding: pandas dataframe
        '''

        model = SentenceTransformer(self.requested_transformer)
        assert corpus is not None
        embedding = model.encode(corpus)
        sim_matrix = self.supported_distances[self.requested_distance_func](embedding)
        embedding_df = pd.DataFrame(embedding)
        embedding_df.columns = [str(i) for i in range(embedding_df.shape[1])]

        sim_df = pd.DataFrame(sim_matrix, columns=[str(i) for i in range(sim_matrix.shape[1])])

        return embedding_df, sim_df
        