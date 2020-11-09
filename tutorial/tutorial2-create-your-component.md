# Tutorial 2: Create your own component

In [tutorial 1](./tutorial1-use-existing-components.md), you learned how to use an existing component in the gallery. What if the component you want is not in the gallery? You can create your own component and share it in the gallery with others. This tutorial will walk through how to create your own component.

This tutorial will use the NYC Taxi Fare Prediction as an example. The pipeline structure will looks like below. We will provide source code and component spec for the clean and merge component. Your task is to train a XGBoost model with the processed data. 

1. Register NYC taxi data as AML dataset for following use
1. Clean the data with clean component
1. Merge the cleaned data with Merge component
1. Train a XGBoost model 
1.  