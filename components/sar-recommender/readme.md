# Simple Algorithm for Recommender

Simple Algorithm for Recommendation (SAR) is a fast and scalable algorithm for personalized recommendations based on user transaction history. It produces easily explainable and interpretable recommendations and handles "cold item" and "semi-cold user" scenarios. SAR is a kind of neighborhood based algorithm (as discussed in Recommender Systems by Aggarwal) which is intended for ranking top items for each user. More details about SAR can be found in the deep dive notebook.

SAR recommends items that are most similar to the ones that the user already has an existing affinity for. Two items are similar if the users that interacted with one item are also likely to have interacted with the other. A user has an affinity to an item if they have interacted with it in the past.

## Component spec

SAR contains following components:
- [Stratified Splitter](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/stratified_splitter.yaml): split dataset into training dataset and test dataset. - [SAR Training](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/sar_train.yaml): Train a simple algorithm recommender. 
- [SAR Scoring](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/sar_score.yaml): using test dataset to score the trained recommender. 
- [MAP](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/map.yaml): Mean Average Precision at K metric. 
- [nDCG](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/ndcg.yaml): Normalized Discounted Cumulative Gain (nDCG) at K metric.
- [Precision at K](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/precision_at_k.yaml): Precision at K metric.
- [Recall at K](https://github.com/microsoft/recommenders/blob/andreas/hyperdrive/reco_utils/azureml/azureml_designer_modules/module_specs/recall_at_k.yaml): Recall at K metric.

## Create new component in your workspace

In the Azure Machine Learning studio portal, you can create new component in your workspace and use it in the designer.
1. Go to **Modules** asset page.
1. Click on **New Module** and select **From Yaml file**.
1. Input the component spec URL and Click **Next**
1. Follow the guidance to finish your creation. And You could find your new components under **Custom Module** in the module list of Designer.