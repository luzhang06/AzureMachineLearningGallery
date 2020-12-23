# Azure Machine Learning Gallery

Azure Machine Learning Gallery enables our growing community of developers and data scientists to share their machine learning pipelines, components, etc. to accelerate productivity in the machine learning lifecycle.

In this gallery, you can easily find a machine learning pipeline/component which is similar to the problem you are trying to solve, rather than starting from scratch.



## Component samples

| Algorithm | Description |
| --- | --- |
|[Simple Algorithm for Recommendation (SAR)*](./pipelines/sar-pipeline) | An example of how to train, score and evaluate an SAR recommender using the Azure Machine Learning component. </br> This scenario contains the following components: </br> [Stratified Splitter](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/stratified_splitter.yaml): split dataset into training dataset and test dataset. </br> [SAR Training](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/sar_train.yaml): Train a simple algorithm recommender. </br> [SAR Scoring](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/sar_score.yaml): using test dataset to score the trained recommender. </br> [MAP](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/map.yaml): Mean Average Precision at K metric. </br> [nDCG](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/ndcg.yaml): Normalized Discounted Cumulative Gain (nDCG) at K metric. </br> [Precision at K](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/precision_at_k.yaml): Precision at K metric. </br> [Recall at K](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/recall_at_k.yaml): Recall at K metric. 
|[Spectral Residual Anomaly Detection](./pipelines/ad-pipeline)| Anomaly detection aims to discover unexpected events or rare items in data. It is designed to be accurate, efficient and general, using Spectral Residual (SR) and Convolutional Neural Network (CNN).
| [Text classification using CNN](./pipelines/textcnn-pipeline) | An example of how to train, and score a CNN sentiment classifier using combination of Designer built-in modules and components. </br> This scenario contains the following components:</br> [textCNN Train Model](./components/text-cnn/textcnn-train/train.yaml) </br> [textCNN Score Model](./components/text-cnn/text-score/score.yaml) </br> [TextCNN Word to Id](./components/text-cnn/textcnn-preprocess/preprocess.yaml) </br>
| [Image classification using AML labeling dataset](./pipelines/labeling-image-classification-pipeline) | This scenario contains a component [Convert Labeling Data to Image Directory](./components/convert-labeling-data-to-image-directory/convert_labeling_data_to_image_directory.spec.yaml) to convert AML labeling dataset to ImageDirectory and other built-in modules in Designer, to build an image classification pipeline. |


You can find more components [here](./components)

## Vote for more components

Vote for more components in the [Microsoft Azure forum](https://feedback.azure.com/forums/257792-machine-learning).

You can either vote for existing ideas or post your new idea in the Microsoft Azure Machine Learning channel. If you have specific design and script, feel free to upload in the channel.
Make sure you contain **component**, and **designer** in the title if you post your new ideas.

Existing candidates:

[One-class SVM](https://feedback.azure.com/forums/257792-machine-learning/suggestions/41067847-ask-for-more-unsupervised-models-as-train-anomaly)

[Data validation component](https://feedback.azure.com/forums/257792-machine-learning/suggestions/41931124-data-validation-component-in-azure-machine-learnin)

## Quick Links
* [Pipelines](/pipelines/README.md) - highlights of end to end machine learning workflows in multipe domains like text analytics, computer vision, recommendation, etc.
* [Components](/components/README.md) - a catalog of components which can be reused in different pipelines


## Tutorial
- [Tutorial 1: Use existing component from gallery](./tutorial/tutorial1-use-existing-components.md)
- [Toturial 2: Create your own component](./tutorial/tutorial2-create-your-component.md)
 

## Get Involved
Please email us: azuremldesigner@microsoft.com

## Help & Support

This project uses GitHub Issues to track bugs and feature requests. 

Please search the existing issues before filing new issues to avoid duplicates.  
For new issues, file your bug or feature request as a new Issue. 

Following information are useful for debugging:
- Pipeline run URL
- Pipeline graph
- Detailed error message
- 70_driver_log of failed component

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.

# Containerization Preview Terms of Use

These terms of use apply only to the containerization preview.

This preview is made available to you on the condition that you agree to the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/) which supplement [your agreement](https://azure.microsoft.com/en-us/support/legal/) governing use of Azure.

The preview, including its user interface, features and documentation is confidential and proprietary to Microsoft and its suppliers. For five (5) years after access of this service or its commercial release, whichever is first, you may not disclose confidential information to third parties. You may disclose confidential information only to your employees and consultants who need to know the information. You must have written agreements with them that protect the confidential information at least as much as these terms. Your duty to protect confidential information survives these terms.

You may disclose confidential information in response to a judicial or governmental order. You must first give written notice to Microsoft to allow it to seek a protective order or otherwise protect the information. Confidential information does not include information that (i) becomes publicly known through no wrongful act; (ii) you received from a third party who did not breach confidentiality obligations to Microsoft or its suppliers; or (iii) you developed independently.

If you give feedback about the preview to Microsoft, you give to Microsoft, without charge, the right to use, share and commercialize your feedback in any way and for any purpose. You will not give feedback that is subject to a license that requires Microsoft to license its software or documentation to third parties because Microsoft includes your feedback in them. These rights survive these terms.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

<a href="https://trackgit.com"><img src="https://sfy.cx/u/oAu" alt="trackgit-views" /></a> _views_
