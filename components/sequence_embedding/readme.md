# Sequence embeddings Module
<br>
This module will help with modeling sequence data in Azure Machine Learining designer by extracting short/long term sequence features and generate emebedding in finite-dimensional space. The embeddings can then be used as input to a Machine Learning algorithm.

The module also creates a transformation that you can apply to new data using Score Sequence Embeddings module, to achieve a similar featurization, without requiring additional training.

## How to use it

This experiment show how it can be used for classification task in the designer in Azure Machine Learning Studio

![classification task](https://testmlposte.blob.core.windows.net/cmcaptures/protein_exp.PNG) 


### Reference:



- Article introducing SGT library used in the module https://towardsdatascience.com/sequence-embedding-for-clustering-and-classification-f816a66373fb


### Citations:

```
Ranjan, Chitta, Samaneh Ebrahimi, and Kamran Paynabar. "Sequence Graph Transform (SGT): A Feature Extraction Function for Sequence Data Mining." arXiv preprint arXiv:1608.03533 (2016)

@article{ranjan2016sequence, title={Sequence Graph Transform (SGT): A Feature Extraction Function for Sequence Data Mining}, author={Ranjan, Chitta and Ebrahimi, Samaneh and Paynabar, Kamran}, journal={arXiv preprint arXiv:1608.03533}, year={2016} }
```



