# Tutorial 2: Create your own component

In [tutorial 1](./tutorial1-use-existing-components.md), you learned how to use existing components in the gallery. What if the component you want is not in the gallery? You can create your own component and share it in the gallery with others. This tutorial will help you on how to create a component with a real case example.

## Basis of creating the Azure Machine Learning component

Each Azure Machine Learning component is constituted by 2 parts:
- Component specification in Yaml format (i.e. Yaml Spec).
- Your own code in Python format (i.e. Py Code). 

_Tips: it would be possible to have the 3rd file to describle a component: Conda configuration yaml file. Usually, component owner could put these Conda config inline in Yaml Spec. But Azure Machine Learning Component Yaml Spec also support to reference a exsiting Conda yaml config in the same folder to save the effort for editing._

### Yaml Spec
Yaml spec is the central place to define the component from the following perspectives:
1. Metadata of the component. Available settings are listed here:

| Name                | Type                                                     | Required | Description                                                  |
| ------------------- | -------------------------------------------------------- | -------- | ------------------------------------------------------------ |
| $schema             | String                                                   | Yes      | Specify the version of the schema of spec. Currently Azure Machine learning components only support CommandComponent(i.e. http://azureml/sdk-2-0/CommandComponent.json) |
| name                | String                                                   | Yes      | Name of the component. Name will be unique identifier of the component. Our recommendation to the component name will be something like company.team.name-of-component. Name only accept letters, numbers and -._ |
| version             | String                                                   | Yes      | Version of the component. Could be arbitrary text, but it is recommended to follow the [Semantic Versioning](https://semver.org/) specification. |
| display_name        | String                                                   | No       | Display name of the component. Defaults to same as name. |
| type                | String                                                   | No       | Defines type of the Component. `CommandComponent` is the default value if not specified. |
| description         | String                                                   | No       | Detailed description of the Component. |
| tags                | Dictionary<String>                                       | No       | A list of key-value pairs to describe the different perspectives of the component. Each tag's key and value should be one word or a short phrase, e.g. `Product:Office`, `Domain:NLP`, `Scenario:Image Classification`. |
| is_deterministic    | Boolean                                                  | No       | Specify whether the component will always generate the same result when given the same input data. Defaults to `True` if not specified. Typically for components which will load data from external resources, e.g. Import data from a given url, should set to `False` since the data to where the url points to may be updated. |

2. Interface specifications. `'inputs'` and `'outputs'` are top level settings where you could define custominzed ports and parameters. Each single input/output could also be descible by there sub-settings as below:

| Name         | Type                    | Required | Description                                                  |
| ------------ | ----------------------- | -------- | ------------------------------------------------------------ |
| type         | String or  List<String> | Yes      | Defines the data type(s) of this input. |
| display_name | String                  | No       | Display name of the input port or parameter. |
| optional     | Boolean                 | No       | Indicates whether this input is an optional port. Defaults to `False` if not specified. |
| description  | String                  | No       | Detailed description to the input port.      |


The difference between `'ports'` and `'parameters'` is that all ports will be a linkable point on the component box to facilitate transition between components, but paraments is the customized inputs when create a new instance of this component. All parameters could be set on right panel for a given component.

Currently, ports and parameters are distinguished by their 'type' in each defination. Here is the list for all available types and their classification:

| Name               | Ports/Parameters      | Description                                                  |
| ------------------ | --------------------- | ------------------------------------------------------------ |
| String             | Parameter             | Indicates that the input value is a string.                  |
| Integer            | Parameter             | Indicates that the input value is an integer.                |
| Float              | Parameter             | Indicates that the input value is a float.                   |
| Boolean            | Parameter             | Indicates that the input value is a boolean value.           |
| Enum               | Parameter             | Indicates that the input value is a enumerated (limited list of) String values. |
| AnyDirectory       | Port                  | Generic directory which stores arbitray data                 |
| DataFrameDirectory | Port                  | Represents tabular data, saved in parquet format by default. |
| path               | Port                  | A path contains arbitray data.                               |
| AzureMLDataset     | Port                  | Represents a dataset, passed directly as id in command line. |

_Tips: Currently, Azure Machine Learning Components only support both Port Parameter for the inputs. All outputs should be Port._
_Tips: DataFrameDirectory is the common data interface when using Azure Machine Learning dataset in Designer. This type could be easily transformed against Pandas DataFrame. The best practice here is using DataFrameDirectory to be any data inputs/outputs when you define your components._

3. Command for calling your Py code. For all CommandComponent, set your 1 line command under setting `'command'` to specify the calling of your python code.

_Tips: All inputs and outputs defined should be considered to pass through command args to your python code in this 1 line setting._
_Tips: All optional inputs should be quoted by '[ ]'._

4. Envrionment for your component. Setting `'environment'` is used for defining your environment needs by specify the sub-settins below:

| Name      | Type             | Required | Description                                                  |
| --------- | ---------------- | -------- | ------------------------------------------------------------ |
| docker    | DockerSection    | No       | This section configures settings related to the final Docker image built to the specifications of the environment and whether to use Docker containers to build the environment. |
| conda     | CondaSection     | No       | This section specifies which Python environment and interpreter to use on the target compute. |           |
| os        | String           | No       | Defines the operating system the component running on. Could be `windows` or `linux`. Defaults to `linux` if not specified. |

_Tips: In 'conda' settings, you could paste your conda setting directly or specify your conda file under the same folder with your Yaml Spec._

Here is a Yaml Spec template to elaborate all these settings as an example:

```dotnetcli
#  This is a template component spec yaml file.
#  For more details, please refer to https://aka.ms/azure-ml-component-specs
$schema: http://azureml/sdk-2-0/CommandComponent.json
name: microsoft.com.azureml.samples.YamlTemplate
version: 0.0.1
display_name: Yaml Spec template.
type: CommandComponent
is_deterministic: false
tags:
  Tutorial: Template
inputs:
  input_1_Data_Port:
    type: DataFrameDirectory
    optional: false
  input_2_str_Param:
    type: String
    default: some_string
    optional: true
outputs:
  output_dir:
    type: path
command: >-
  python TutorialTemplate.py
  --input_1_Data_Port {inputs.input_1_Data_Port}
  [--input_2_str_Param {inputs.input_2_str_Param}]
  --output_dir {outputs.output_dir}
environment:
  docker:
    image: mcr.microsoft.com/azureml/intelmpi2018.3-ubuntu16.04
  conda:
    conda_dependencies:
      name: project_environment
      channels:
      - defaults
      dependencies:
      - python=3.7.6
      - pip=20.0
      - pip:
        - azureml-sdk==0.1.0.*
        - azureml-designer-core==0.0.31
        - azureml-dataset-runtime[fuse,pandas]
        - --index-url https://azuremlsdktestpypi.azureedge.net/dev/aml/office/134157926D8F
        - --extra-index-url https://pypi.org/simple
        - pandas
  os: Linux
```

### Py Code
Py code will contain your own logic for processing your data, training model or manage your output. All the inputs of the component (e.g. data port or parameters) should be passed through args. 

Following the Yaml Spec template, here is the corresponding py code example template:

```python
import sys
import argparse
import pandas as pd
from pathlib import Path
from azureml.studio.core.io.data_frame_directory import load_data_frame_from_directory, save_data_frame_to_directory

## Parse inputs/outputs args
parser = argparse.ArgumentParser("TutorialTemplate")
parser.add_argument("--input_1_Data_Port", type=str, help="input 1.")
parser.add_argument("--input_2_str_Param", type=str, help="input 2.")
parser.add_argument("--output_dir", type=str, help="output directory.")
args = parser.parse_args()

## Put your own code here:
df = load_data_frame_from_directory(args.input_1_Data_Port).data
print("input1: " + str(type(df)))
print("str_param: " + args.input_2_str_Param)

## Manage your output
output_dir = Path(output_dir)
with open(output_dir / f"output.txt", 'w') as fout:
    fout.write(str_param)
```

## Example with NYC Taxi Fare Prediction
Let's use a real case for playing with the process to create a real useful component. In tutorial 1, we created a pipeline to process NYC taxi data and we will continue that story by training a model with newly created component.

Before we start the tutorial, let's assume we have a local code for training XGBoost regressor model as below:
```python
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import xgboost as xgb

## Training data preparation
data = pd.read_csv('NYC-taxi-fare.csv')
data.head(10)
data = data.iloc[:,2:7]
data.head()
X, y = data.iloc[:,1:],data.iloc[:,0]

## Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 10)
xg_reg.fit(X_train,y_train)

## Evaluation
preds = xg_reg.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE: %f" % (rmse))

## Output model
xg_reg.save_model('xgb_modelfile.json')
```

### Define the component
Before we start writing Yaml Spec and py code, we need think carefully about the scope for a component. It means we need abstract the core, common functionality from our local code and define its necessary inputs/outputs. In general, the purpose to create a component is to reuse the same code and logic to improve the productivity with sharing in open source galary. In this case, XGBRegressor would be the proper function we plan to package it to a new components in this tutorial. 

It is suggested to start from the interface defination:
- Data inputs. We would assume the data flow into this component is preprocessed by the precedent components with the necessary cleaning and cooking. To run the training and evaluation for xgb.XGBRegressor, we need 4 data inputs:
  - Feature table used for training.
  - Lable vector used for training.
  - Feature table used for evaluation.
  - Lable vector used for evaluation.
- Parameters inputs. When we initiate XGBRegressor every time, we may use different variables. The best practice here is put all these variables into parameters of the component. Then we could easily change them every time without update the component. In this case, we will consider these parameters:
  - colsample_bytree. Subsample ratio of columns when constructing each tree.
  - Learning_rate. Boosting learning rate
  - Max_depth. Maximum tree depth for base learners.
  - N_estimators. Number of trees in random forest to fit.
- outputs. In xgboost SDK, we could output the trained model to a Json file for the futher usage(e.g. offline inference). So we will consider this Jsom model file as the main output. At the meanwhile, evaluation result is also important to judge the performace of a model. We will also output these evaluation result as DataFrameDiretory format to easy preview them in the designer pipeline UI.

Then also condider the environment for supporting this component. xgboost SDK would not be included in the default environment. So we need include this in environment defination.

### Create Yaml Spec
Let's start creating our XGBRegressor component Yaml spec by following the steps
1. Metadata.

    Our XGBRegressor component should also be a CommandComponent and let's use the name 'microsoft.com.azureml.samples.XGBRegressor' for this component. To simplify on the UI, we could also give its 'display_name' as XGBRegressor. We'd like also add a 'Tutorial' tag to this component to help us understand the purpose of this component. 

    The Yaml content for this metadata defination would be:
```dotnetcli
$schema: http://azureml/sdk-2-0/CommandComponent.json
name: microsoft.com.azureml.samples.XGBRegressor
version: 0.0.1
display_name: XGBRegressor
type: CommandComponent
is_deterministic: false
tags:
  Tutorial:
```
2. Interface.

  - For every data input in our XGBRegressor component, we need use 'DataFrameDirectory' as its type. Given our training/evaluation could not run with any missing of these data, we should set 'optional' to false. An example as below:
```dotnetcli
Training_Data_Features:
    type: DataFrameDirectory
    optional: false
```

  - For every parameter input in our XGBRegressor component, it is also suggested to give them an default value and description to help others understand the meanning when they initiate this component through Designer UI. An example as below:
```dotnetcli
Colsample_bytree:
    type: Float
    default: 0.3
    optional: false
    description: Subsample ratio of columns when constructing each tree.
```

  - Also define our XGBRegressor output as designed below:
```dotnetcli
outputs:
  Model_Path:
    type: path
  Evaluation_Result:
    type: DataFrameDirectory
```

3. Commandline.

    Considering the interface of our XGBRegressor component, include them into our command line when calling our component:
```dotnetcli
command: >-
  python XGBRegressor.py 
  --Training_Data_Features {inputs.Training_Data_Features} 
  --Training_Data_Lable {inputs.Training_Data_Lable} 
  --Evaluation_Data_Features {inputs.Evaluation_Data_Features} 
  --Evaluation_Data_Lable {inputs.Evaluation_Data_Lable} 
  --Colsample_bytree {inputs.Colsample_bytree} 
  --Learning_rate {inputs.Learning_rate}
  --Max_depth {inputs.Max_depth} 
  --N_estimators {inputs.N_estimators}
  --Model_Path {outputs.Model_Path} 
  --Evaluation_Result {outputs.Evaluation_Result}
```
4. Envrionment.

    To draft envrionment of our XGBRegressor component, we could start from copy the template and enrich the dependencies for our needs. e.g. install xgboost under conda pip section. 
```dotnetcli
environment:
  docker:
    image: mcr.microsoft.com/azureml/intelmpi2018.3-ubuntu16.04
  conda:
    conda_dependencies:
      name: project_environment
      channels:
      - defaults
      dependencies:
      - python=3.7.6
      - pip=20.0
      - pip:
        - azureml-sdk==0.1.0.*
        - azureml-designer-core==0.0.31
        - azureml-dataset-runtime[fuse,pandas]
        - --index-url https://azuremlsdktestpypi.azureedge.net/dev/aml/office/134157926D8F
        - --extra-index-url https://pypi.org/simple
        - pyarrow
        - pandas
        - scikit-learn
        - numpy
        - xgboost
  os: Linux
```

After following the 4 steps, we now have our full Yaml spec for XGBRegressor component as below:
```dotnetcli
#  This is a tutorial component spec yaml file for XGBRegressor.
#  For more details, please refer to https://aka.ms/azure-ml-component-specs
$schema: http://azureml/sdk-2-0/CommandComponent.json
name: microsoft.com.azureml.samples.XGBRegressor
version: 0.0.3
display_name: XGBRegressor
type: CommandComponent
is_deterministic: false
tags:
  Tutorial:
inputs:
  Training_Data_Features:
    type: DataFrameDirectory
    optional: false
  Training_Data_Lable:
    type: DataFrameDirectory
    optional: false
  Evaluation_Data_Features:
    type: DataFrameDirectory
    optional: false
  Evaluation_Data_Lable:
    type: DataFrameDirectory
    optional: false
  Colsample_bytree:
    type: Float
    default: 0.3
    optional: false
    description: Subsample ratio of columns when constructing each tree.
  Learning_rate:
    type: Float
    default: 0.1
    optional: false
    description: Boosting learning rate
  Max_depth:
    type: Integer
    default: 5
    optional: false
    description: Maximum tree depth for base learners.
  N_estimators:
    type: Integer
    default: 10
    optional: false
    description: Number of trees in random forest to fit.
outputs:
  Model_Path:
    type: path
  Evaluation_Result:
    type: DataFrameDirectory
command: >-
  python XGBRegressor.py 
  --Training_Data_Features {inputs.Training_Data_Features} 
  --Training_Data_Lable {inputs.Training_Data_Lable} 
  --Evaluation_Data_Features {inputs.Evaluation_Data_Features} 
  --Evaluation_Data_Lable {inputs.Evaluation_Data_Lable} 
  --Colsample_bytree {inputs.Colsample_bytree} 
  --Learning_rate {inputs.Learning_rate}
  --Max_depth {inputs.Max_depth} 
  --N_estimators {inputs.N_estimators}
  --Model_Path {outputs.Model_Path} 
  --Evaluation_Result {outputs.Evaluation_Result}
environment:
  docker:
    image: mcr.microsoft.com/azureml/intelmpi2018.3-ubuntu16.04
  conda:
    conda_dependencies:
      name: project_environment
      channels:
      - defaults
      dependencies:
      - python=3.7.6
      - pip=20.0
      - pip:
        - azureml-sdk==0.1.0.*
        - azureml-designer-core==0.0.31
        - azureml-dataset-runtime[fuse,pandas]
        - --index-url https://azuremlsdktestpypi.azureedge.net/dev/aml/office/134157926D8F
        - --extra-index-url https://pypi.org/simple
        - pyarrow
        - pandas
        - scikit-learn
        - numpy
        - xgboost
  os: Linux
```
### Prepare Py Code
Upgrade our local py code to module py code is much easier than create Yaml spec. We just need 3 steps based on our local code:
- Import necessary Azure Machine Learning libs. e.g. azureml.studio.core.io.data_frame_directory to support DataFrameDirectory.
- Parse all inputs from args and call XGBRegressor training with these input values. 
- Create output folders and write the result to those location.

Following the Py Code template and our component defination, here is the full Py code for XGBRegressor component:
```python
import os
import sys
import argparse
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.metrics import mean_squared_error

from azureml.studio.core.io.data_frame_directory import load_data_frame_from_directory, save_data_frame_to_directory

import xgboost as xgb

## Parse args
parser = argparse.ArgumentParser("XGBRegressor")
parser.add_argument("--Training_Data_Features", type=str, help="Features of training dataset.")
parser.add_argument("--Training_Data_Lable", type=str, help="Lable of training dataset.")
parser.add_argument("--Evaluation_Data_Features", type=str, help="Features of evaluation dataset.")
parser.add_argument("--Evaluation_Data_Lable", type=str, help="Lable of evaluation dataset.")

parser.add_argument("--Colsample_bytree", type=float, help="Subsample ratio of columns when constructing each tree.")
parser.add_argument("--Learning_rate", type=float, help="Boosting learning rate.")
parser.add_argument("--Max_depth", type=int, help="Maximum tree depth for base learners.")
parser.add_argument("--N_estimators", type=int, help="Number of trees in random forest to fit.")
parser.add_argument("--Model_Path", type=str, help="Path to store XGBoost model file in Json format.")
parser.add_argument("--Evaluation_Result", type=str, help="Evaluation result")

args = parser.parse_args()

## Load data from DataFrameDirectory to Pandas DataFrame
training_df_features = load_data_frame_from_directory(args.Training_Data_Features).data
training_df_lable = load_data_frame_from_directory(args.Training_Data_Lable).data
evaluation_df_features = load_data_frame_from_directory(args.Evaluation_Data_Features).data
evaluation_df_lable = load_data_frame_from_directory(args.Evaluation_Data_Lable).data

## Training
xg_reg = xgb.XGBRegressor(
                objective ='reg:linear', 
                colsample_bytree = args.Colsample_bytree, 
                learning_rate = args.Learning_rate,
                max_depth = args.Max_depth, 
                alpha = 10, 
                n_estimators = args.N_estimators)

xg_reg.fit(training_df_features, training_df_lable)

## Evaluation
preds = xg_reg.predict(evaluation_df_features)
rmse = np.sqrt(mean_squared_error(evaluation_df_lable, preds))
print("RMSE: %f" % (rmse))

## Output model and evaluation result
os.makedirs(args.Model_Path, exist_ok=True)
xg_reg.save_model(args.Model_Path + "/xgb_modelfile.json")

eva_result_df = pd.DataFrame(np.array([rmse]), columns=['RMSE Result'])
os.makedirs(args.Evaluation_Result, exist_ok=True)
save_data_frame_to_directory(args.Evaluation_Result, eva_result_df)
```

### Register XGBRegressor component to Designer
After have the Yaml Spec and Py code ready, we could follow the major register path in Tutorial1 to register our XGBRegressor component through Azure Machine Learning Component page. The only difference is you need register the component from 'Local files' where contains your Yaml Spec and Py code as below:

![create-component-from-localfiles](./create-component-from-localfiles.PNG)


[Note] It would be suggested to put these 2 files together in same folder. Else you need manage the relative path in your spec.

Then click 'Next' and 'Create' for finish the creation of XGBRegressor component. You will see the newly created component in both Component page and Designer authoring page.

![component-description](./component-description.PNG)
![component-in-designer](./component-in-designer.PNG)

### Register XGBRegressor component to Galary
TBD




