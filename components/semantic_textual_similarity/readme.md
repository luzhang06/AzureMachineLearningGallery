# Semantic textual similarity

This module derive sentence embedding using  state of the art fine tuned transformers  BERT / RoBERTa / DistilBERT with a siamese or triplet network structure to produce semantically meaningful sentence embeddings.

The module produces sentence embedding that can be used for supervided learning task or unsupervised learning such as clustering, but also similarity matrix that can be calculated using several distance metrics to choose from.


# How to use it

Simply connect your dataset to the module, specify the text column, choose the transformer network to use and the distance metric you'd like for similarity matrix calculation

Here is an example that shows how the module can be use for a classification task and clustering.

![example](https://testmlposte.blob.core.windows.net/cmcaptures/sts.PNG) 

# References & Citation
- https://github.com/UKPLab/sentence-transformers

```
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "http://arxiv.org/abs/1908.10084",
}