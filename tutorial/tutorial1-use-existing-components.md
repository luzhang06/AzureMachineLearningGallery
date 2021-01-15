# Tutorial 1: Use existing components from gallery

A component is self-contained set of code that performs one step in machine learning pipeline, such as data preprocessing, model training, model scoring and so on. A component is analogous to a function, in that it has a name, parameters, expects certain input and returns some value. Any python script can be wrapped as a component following the [component spec](component-spec-definition.md).

Azure Machine Learning Gallery contains rich components and pipelines for common machine learning tasks. It can accelerate AI adoption by enabling enterprises and individuals to easily leverage best work of the community instead of starting from scratch.

In this tutorial, you will learn how to build a machine learning pipeline with existing components in the gallery in 2 steps:
 1. Register the component to your Azure Machine Learning workspace.
 2. Build a pipeline using the registered component and built-in modules in Azure Machine Learning designer.

> **! NOTE:**  
>
> **Components** equals to **Modules** in Azure Machine Learning studio UI.

This tutorial will use Automobile Price Prediction as an example. The related components can be found under components/automobile-price-prediction.


## 1. Register existing components from gallery to your workspace

To use components from this gallery and build a pipeline, you need to register components to your Azure Machine Learning workspace first.

This tutorial will explain how to register component from the gallery with a sample component - XGBRegressorTraining under folder [components/automobile-price-prediction](../components/automobile-price-prediction).

1. Go to https://ml.azure.com and select your workspace.

    > **! NOTE:**  
    >
    > Please open the designer before you do following steps if you have never opened it in your workspace before. This is to make sure the required data types are registered to the workspace so that you can register components successfully to workspace.  

1. Add **&flight=cm** at end of the URL of your workspace to enable components feature. You will see **Modules** tab under Assests blade on the left navigation bar. 

    ![create-component](./img/aml-studio-flight.png)
    
1. Click *Create -> From YAML file*. Choose Github repo as source. Fill in the URL of cleanse component YAML spec file (https://github.com/Azure/AzureMachineLearningGallery/blob/main/components/automobile-price-prediction/xgboost-regressor-training/XGBRegressorTraining.spec.yaml).

    > **! NOTE:**  
    >
    > If you have created components in your workspace before, click *New Module -> From YAML file* to create a new component.

    ![create-component](./img/create-component.png)
    

1. Follow the wizard to finish the creation. 
    
    After creation, you will see the component both in component asset page for management.

    ![component-page](./img/component-page.png)
   


## 2. Use registered component to build pipeline in designer

Azure Machine Learning designer is the UI to build machine learning pipelines. It provides an easy drag-n-drop interface to build, test and manage your machine learning pipelines.

1. Open a new pipeline in the designer. You can find the registered component under **Custom Module** category in Designer module palette.

    ![registered-component](./img/module-tree.png)

1. Find **Automobile price data (Raw)** dataset under **Sample datasets** in the asset library to the left of canvas and drag it to canvas. Then you can right click the dataset and click **Visualize** to preview the data.

1. Drag the following components/moudles to canvas and config parameters in right panel of each component/module as following:

    |Module|Parameter|
    |---|---|
    |**Select Columns in Dataset**| Click **Edit column**, and select Include **Column types** -> **Numeric**. This is because this XGBRegressor component can only process numeric features.
    |**Clean Missing Data**| Click **Edit column**, and select Include **All columns**. This is to clean missing data in the dataset. </br> **Cleaning mode**: select *Remove entire row* to remove rows with missing value.
    |**Split Data**| **Splitting mode** is by default set as *Split Rows*. </br> **Fraction of rows in the first output dataset**: You can set split fraction of the input data.
    |**XGBRegressorTraining**| **Label_Col**: Input *price* - the label column name.</br> **Model_FileName**: Input the output model name, e.g.`xgb_modelfile.json`.</br> **Learning_rate**: Set the learning rate of XGBRegressor, by default 0.1. </br> **Max_depth**: Maximum tree depth for base learners, by default 5.


1. Connect them to build the pipeline as shown below. 

    ![tutorial1-pipeline](./img/tutorial1-pipeline.png)

1. Submit a run.
    
    Select a compute target and submit a run. 

1. Check result of the run.
    
    If the run finishes successfully, each component's output will be stored in the workspace's default blob. 
    You can access the output in storage account by **View Output** in the right click menu of the component. The output is a json file of the trained XGBRegressor.

    If the run fails, check the 70_driver_log under Outputs + Logs to troubleshot. 
  




## Next step
This tutorial walks you through how to use existing components from the gallery to build a machine learning pipeline. Follow the [second part of the tutorial](./tutorial2-create-your-component.md) to learn how to create a component with your own code. 
