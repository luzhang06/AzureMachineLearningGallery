# Pipeline gallery
This gallery highlights using Azure Machine Learning pipeline with components to build, optimize, and manage machine learning workflows. [Learn more](https://docs.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines).


![](https://docs.microsoft.com/en-us/azure/machine-learning/media/concept-designer/designer-drag-and-drop.gif)
[Azure Machine Learning designer](https://azure.microsoft.com/services/machine-learning/designer/) lets you visually connect datasets and components on an interactive canvas to create machine learning models. You can also use the [Python SDK](https://docs.microsoft.com/python/api/overview/azure/ml/?view=azure-ml-py) to construct a pipeline.

## Pipeline samples

| Scenario |  Description |
| --- | --- |
| [Text Classification with CNN](./textcnn-pipeline/README.md) | Text classification pipeline - Demonstrates how to train and score models with component SDK 
| [Simple Algorithm Recommender](./sar-pipeline/README.md) | SAR pipeline - Example of how to train, score and evaluate an SAR recommender 
| [Spectral Residual Anomaly Detection](./ad-pipeline/README.md) | Anomaly Detection pipeline - Example of how to build Spectral Residual Anomaly Detection model 
| [Image classification using AML labeling dataset](./labeling-image-classification-pipeline/README.md) | Image classification pipeline - Shows how to use convert a labeled dataset to image directory and then use Designer built-in modules to build image classification model|

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

