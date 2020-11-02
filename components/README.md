# Component gallery
In this directory, you will find a wide array of components that can be used in Azure Machine Learning, contributed by Microsoft and open source community. 

## Components
A component is self-contained set of code that performs one step in the ML workflow (pipeline), such as data preprocessing, model training, model scoring and so on. A component is analogous to a function, in that it has a name, parameters, expects certain input and returns some value. Data scientists or developers can wrap their arbitrary code as Azure Machine Learning component by following the component specification. Find the tutorials [TODO](https://aka.ms/aml-component) to get started.

A component

Following are some available components in the gallery.

| Scenario | Type | Description |
| --- | --- | --- |
|[Simple Algorithm for Recommendation (SAR)*](https://github.com/microsoft/recommenders/tree/master/examples/00_quick_start) | Algorithm | An example of how to train, score and evaluate an SAR recommender using the Azure Machine Learning component. </br> This scenario contains the following components: </br> [Stratified Splitter](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/stratified_splitter.yaml): split dataset into training dataset and test dataset. </br> [SAR Training](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/sar_train.yaml): Train a simple algorithm recommender. </br> [SAR Scoring](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/sar_score.yaml): using test dataset to score the trained recommender. </br> [MAP](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/map.yaml): Mean Average Precision at K metric. </br> [nDCG](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/ndcg.yaml): Normalized Discounted Cumulative Gain (nDCG) at K metric. </br> [Precision at K](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/precision_at_k.yaml): Precision at K metric. </br> [Recall at K](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/recall_at_k.yaml): Recall at K metric. 
|[Spectral Residual Anomaly Detection](https://github.com/microsoft/anomalydetector/tree/master/aml_module#spectral-residual-anomaly-detection-module)| Services | Anomaly detection aims to discover unexpected events or rare items in data. It is designed to be accurate, efficient and general, using Spectral Residual (SR) and Convolutional Neural Network (CNN).
| [Text classification using CNN](./text-cnn) | Algorithms | An example of how to train, and score a CNN sentiment classifier using combination of Designer built-in modules and components. </br> This scenario contains the following components:</br> [textCNN Train Model]() </br> [textCNN Score Model]() </br> [TextCNN Word to Id]() </br> |

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Reference papers
- Ren, Hansheng et al. “Time-Series Anomaly Detection Service at Microsoft.” Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining (2019): n. pag. Crossref. Web.


<a href="https://trackgit.com">
<img src="https://sfy.cx/u/oFs" alt="trackgit-views" />
</a> views