# Component gallery
In this directory, you will find a wide array of components that can be used in Azure Machine Learning, contributed by Microsoft and open source community. 

## Components
A component is self-contained set of code that performs one step in the ML workflow (pipeline), such as data preprocessing, model training, model scoring and so on. A component is analogous to a function, in that it has a name, parameters, expects certain input and returns some value. Data scientists or developers can wrap their arbitrary code as Azure Machine Learning component by following the component specification. Find the [tutorials](../tutorial) to get started.

Following are some available components in the gallery.

| Scenario |Description |
| --- | --- |
|[Simple Algorithm for Recommendation (SAR)*](../pipelines/sar-pipeline/README.md) | An example of how to train, score and evaluate an SAR recommender using the Azure Machine Learning component. </br> This scenario contains the following components: </br> [Stratified Splitter](https://github.com/microsoft/recommenders/blob/staging/reco_utils/azureml/azureml_designer_modules/module_specs/stratified_splitter.yaml): split dataset into training dataset and test dataset. </br> [SAR Training](https://github.com/microsoft/recommenders/blob/staging/reco_utils/azureml/azureml_designer_modules/module_specs/sar_train.yaml): Train a simple algorithm recommender. </br> [SAR Scoring](https://github.com/microsoft/recommenders/blob/staging/reco_utils/azureml/azureml_designer_modules/module_specs/sar_score.yaml): using test dataset to score the trained recommender. </br> [MAP](https://github.com/microsoft/recommenders/blob/staging/reco_utils/azureml/azureml_designer_modules/module_specs/map.yaml): Mean Average Precision at K metric. </br> [nDCG](https://github.com/microsoft/recommenders/blob/staging/reco_utils/azureml/azureml_designer_modules/module_specs/ndcg.yaml): Normalized Discounted Cumulative Gain (nDCG) at K metric. </br> [Precision at K](https://github.com/microsoft/recommenders/blob/staging/reco_utils/azureml/azureml_designer_modules/module_specs/precision_at_k.yaml): Precision at K metric. </br> [Recall at K](https://github.com/microsoft/recommenders/blob/staging/reco_utils/azureml/azureml_designer_modules/module_specs/recall_at_k.yaml): Recall at K metric. 
|[Spectral Residual Anomaly Detection](../pipelines/ad-pipeline/README.md)| Anomaly detection aims to discover unexpected events or rare items in data. It is designed to be accurate, efficient and general, using Spectral Residual (SR) and Convolutional Neural Network (CNN).
| [Text classification using CNN](../pipelines/textcnn-pipeline/README.md) | An example of how to train, and score a CNN sentiment classifier using combination of Designer built-in modules and components. </br> This scenario contains the following components:</br> [textCNN Train Model](./text-cnn/textcnn-train/train.yaml) </br> [textCNN Score Model](./text-cnn/text-score/score.yaml) </br> [TextCNN Word to Id](./text-cnn/textcnn-preprocess/preprocess.yaml) </br> 
| Dimensionality Reduction | This component is based on scikit-learn. You can use [Dimensionality Reduction](./dimensionality_reduction/module_specs/pca_train_component.yaml) to reduce reduce the dimensionality of your data, and [Score Dimensionality Reduction](./dimensionality_reduction/pca_score_component.yaml) to apply the trained transformation on your scoring dataset.
| [Compute Correlation](./compute_correlation/compute_correlation_component.yaml) | Compute correlation matrix of pairwise columns in dataset using kendall, spearman, pearson methods. 
| [Image classification using AML labeling data](../pipelines/labeling-image-classification-pipeline/README.md) | This example use AML labeling dataset as training dataset of image classification. The pipeline contains one custom component [Convert Labeling Data to Image Directory](./convert-labeling-data-to-image-directory/convert_labeling_data_to_image_directory.spec.yaml) and several Designer built-in modules. 
| Natural Language Processing | There are following sample components in NLP scenario: </br> [Detect languages](./detect_languages/languages_component.yaml): Detect languages on text columns in a dataset. </br> [Semantic Textual Similarity](./semantic_textual_similarity/sts_component.yaml) </br> [Sequence Embedding](./sequence_embedding/sgt_train_component.yaml): Model sequence data by extracting short/long term sequence features and generate emebedding in finite-dimensional space. </br> [Score Sequence Embeddings](./sequence_embedding/sgt_score_component.yaml): Apply sequence embeddings to score data using transformation state from training dataset. |

## Create new component in your workspace

In the Azure Machine Learning studio portal, you can create new component in your workspace and use it in the designer.
1. Go to **Modules** asset page.
1. Click on **New Module** and select **From Yaml file**.
1. Input the component spec URL and Click **Next**
1. Follow the guidance to finish your creation. And You could find your new components under **Custom Module** in the module list of Designer.


## Help & Support

This project uses GitHub Issues to track bugs and feature requests. 

Please search the existing issues before filing new issues to avoid duplicates.  
For new issues, file your bug or feature request as a new Issue. 

Following information are useful for debugging:
- Pipeline run URL
- Pipeline graph
- Detailed error message
- 70_driver_log of failed component


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