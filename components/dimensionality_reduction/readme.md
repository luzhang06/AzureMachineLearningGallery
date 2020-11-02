# Dimensionality reduction module

<br>

As the name suggest, the module purpose is to reduce the dimensionality of your training data. The module provides four type of algorithms:

- Linear PCA
- Incremental PCA
- Sparse PCA
- Kernel PCA

For more details on each decomposition and it's hyperparameters, checkout scikit-learn documentation https://scikit-learn.org/stable/modules/decomposition.html

The module also creates a transformation that you can apply to new data using Score Dimensionality Reduction module, to achieve a similar reduction in dimensionality and compression of features, without requiring additional training.

## How to use it

Simply connect your dataset to the module, just make sure that you  filter a priori numeric data only and remove or impute missing values.

![Decomposition](https://testmlposte.blob.core.windows.net/cmcaptures/pca.PNG) 



