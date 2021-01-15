Definition of component spec
==================================

This document describes the specification to define an AzureML component. The spec should be in YAML file format.


### Component Definition

| Name                | Type                                                     | Required | Description                                                  |
| ------------------- | -------------------------------------------------------- | -------- | ------------------------------------------------------------ |
| $schema             | String                                                   | Yes      | Specify the version of the schema of spec. Example: http://azureml/sdk-2-0/CommandComponent.json |
| name                | String                                                   | Yes      | Name of the component. Name will be unique identifier of the component. |
| version             | String                                                   | Yes      | Version of the component. Could be arbitrary text, but it is recommended to follow the [Semantic Versioning](https://semver.org/) specification. |
| display_name        | String                                                   | No       | Display name of the component. Defaults to same as name. |
| type                | String                                                   | No       | Defines type of the Component. Could be `CommandComponent`, `ParallelComponent`, `PipelineComponent`, etc.. Defaults to `CommandComponent` if not specified. |
| description         | String                                                   | No       | Detailed description of the Component. |
| tags                | Dictionary<String>                                       | No | A list of key-value pairs to describe the different perspectives of the component. Each tag's key and value should be one word or a short phrase, e.g. `Product:Office`, `Domain:NLP`, `Scenario:Image Classification`. |
| is_deterministic    | Boolean                                                  | No       | Specify whether the component will always generate the same result when given the same input data. Defaults to `True` if not specified. Typically for components which will load data from external resources, e.g. Import data from a given url, should set to `False` since the data to where the url points to may be updated. |
| inputs              | Dictionary<String, [Input](#Input) or [Parameter](#Parameter)> | No       | Defines input ports and parameters of the component. The string key is the name of Input/Parameter, which should be a valid python variable name. |
| outputs             | Dictionary<String, [Output](#Output)>                    | No       | Defines output ports of the component. The string key is the name of Output, which should be a valid python variable name. |
| code                | String                                                   | No       | Location of the [Code](#Code) snapshot. |
| environment         | [Environment](#Environment)                              | No       | An Environment defines the runtime environment for the component to run. Refer to [here](component-spec-topics/running-environment.md) for details. |
| command             | String                                             | No    | Specify the command to start to run the component code.         |
| parallel | [Parallel](#Parallel [not ready for use]) | No | Settings for `ParallelComponent` only. Refer to [here](#Parallel [not ready for use]) for details. |

### Name

Our recommendation to the component name will be something like `company`.`team`.`name-of-component`.
Current constraint for name: only accept letters, numbers and -._

Sample names:

```
microsoft.office.smart-compose
my-awesome-components.ner-bert
```

Builtin component name will be prefixed with `azureml://`.

Sample names:
```
azureml://Select Columns in Dataset
```

### Description

Please note if you write markdown in description, our portal UX will display a nicely formatted description.
For example: 
```
description: |
  # A dummy training module
  - list 1
  - list 2
```

The above example use ***literal*** style with the indicator `|` to write multil-line in yaml.

See [reference](https://yaml-multiline.info/) for more details of the yaml multi-line format.

### Code

A code snapshot can be expressed as one of 3 things:

      1. a local file path relative to the file where it is referenced e.g. '../'. Register Only support this form now.
      2. an http url e.g. 'http://github.com/foo/bar/dir#239870234080'
      3. a snapshot id, e.g.: aml://6560575d-fa06-4e7d-95fb-f962e74efd7a/azml-rg/sandbox-ws/snapshots/293lkw0j23fw8cv.

### Tags
Some convention tags used by azure-ml-component package. Refer to [get-started-train](../samples/get-started-train/train.yaml) and [get-started-score](../samples/get-started-score/score.yaml) for more details.
| Name        | Type         | Required | Description                                                  |
| ----------- | ------------ | -------- | ------------------------------------------------------------ |
| codegenBy | String | No  | The component spec might be generated by some automation tool. Set the tool name into this field. e.g. `dsl.component` |
| contact     | String       | No       | The contact info of the component's author. Typically contains user or organization's name and email. e.g. `AzureML Studio Team <stcamlstudiosg@microsoft.com>`. |
| helpDocument | String       | No       | The url of the component's documentation. The url is shown as a link on AzureML Designer's page. |

### Input

Defines an input port of the component. Refer to [here](component-spec-topics/inputs-and-outputs.md) for details.

| Name         | Type                    | Required | Description                                                  |
| ------------ | ----------------------- | -------- | ------------------------------------------------------------ |
| type         | String or  List<String> | Yes      | Defines the data type(s) of this input port. Refer to [Data Types for Inputs/Outputs](#data-types-for-inputs/outputs) for details. |
| display_name | String                  | No      | Display name of the input port. |
| optional     | Boolean                 | No       | Indicates whether this input is an optional port. Defaults to `False` if not specified. |
| description  | String                  | No       | Detailed description to the input port.      |

### Parameter

Defines a parameter of the component. Refer to [here](component-spec-topics/inputs-and-outputs.md) for details.

| Name         | Type    | Required | Description                                                  |
| ------------ | ------- | -------- | ------------------------------------------------------------ |
| type         | String  | Yes      | Defines the type of this data. Refer to [Data Types for Parameters](#data-types-for-parameters) for details. |
| display_name | String  | No      | Display name of the parameter. |
| optional     | Boolean | No       | Indicates whether this input is optional. Default value is `False`. |
| default      | Dynamic | No       | The default value for this parameter. The type of this value is dynamic. e.g. If `type` field in Input is `Integer`, this value should be `Inteter`. If `type` is `String`, this value should also be `String`. This field is optional, defaults to `null` or `None` if not specified. |
| description  | String  | No       | Detailed description to the parameter.                       |
| min          | Numeric | No       | The minimum value that can be accepted. This field only takes effect when `type` is `Integer` or `Float`. Specify `Integer` or `Float` values accordingly. |
| max          | Numeric | No       | The maximum value that can be accepted. Similar to `min`.    |
| enum  | List    | No       | The acceptable values for the parameter. This field only takes effect when `type` is `Enum`. |


### Output

Defines an output port of the component. Refer to [here](component-spec-topics/inputs-and-outputs.md) for details.

| Name         | Type   | Required | Description                                                  |
| ------------ | ------ | -------- | ------------------------------------------------------------ |
| name         | String | Yes      | Name of the output port. This field is used for program logic and cannot be duplicated with other inputs of the component. |
| type         | String | Yes      | Defines the data type(s) of this output port. Refer to [Data Types for Inputs/Outputs](#data-types-for-inputs/outputs) for details. |
| display_name | String | No       | Display name of the parameter.                               |
| description  | String | No       | Detailed description to the output port.                     |

### Command

Command is a string which specify the command line to run the component.
It is expected to be a ***one-line string*** in which the arguments are separated by spaces.
The string will be split to a command list according to the shell split rule with the python built-in function [shlex.split](https://docs.python.org/3/library/shlex.html).

Example:

```yaml
command: >-
  python basic_component.py
  --input_dir {inputs.input_dir}
  --str_param {inputs.str_param}
  --enum_param {inputs.enum_param}
  --output-eval-dir {outputs.output_dir}
```

#### Yaml String Format
In the yaml file, it is recommended to use the ***folded*** style with the indicator `>-` to write a one-line string as multiple lines.

If the ***literal*** style with the indicator `|` is used, the command will contain `\n`, which could be handled, but is not recommended.

Unlike programming languages, yaml doesn't use `\` to indicate an unfinished line but treats it as a normal character. A `\` at the end of one line is not recommended since it could not be recognized as an unfinished line in a yaml string.

See [reference](https://yaml-multiline.info/) for more details of the yaml multi-line format.

#### CLI Argument Place Holders

When invoking from a CLI interface, the arguments are specified with placeholders like `{inputs.input_dir}`. The placeholders will be replaced with the actual value when running.

For example, when we set `input_dir='./input'`, the command `--input_dir {inputs.input_dir}` will be replaced as `--input_dir ./input`.

Placeholders are with this format: `inputs.input_name`/`outputs.output_name`.

### Environment

An Environment defines the runtime environment for the component to run, it is equivalent with the definition of the [Environment class in python SDK](https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.environment%28class%29?view=azure-ml-py).

| Name      | Type                    | Required | Description                                                  |
| --------- | ----------------------- | -------- | ------------------------------------------------------------ |
| docker | DockerSection | No       | This section configures settings related to the final Docker image built to the specifications of the environment and whether to use Docker containers to build the environment. |
| conda | CondaSection | No       | This section specifies which Python environment and interpreter to use on the target compute. |           |
| os        | String                  | No       | Defines the operating system the component running on. Could be `windows` or `linux`. Defaults to `linux` if not specified. |


#### DockerSection

| Name      | Type   | Required | Description                                                  |
| --------- | ------ | -------- | ------------------------------------------------------------ |
| image | String | No       | The base image used for Docker-based runs. Example value: "ubuntu:latest". If not specified, will use `mcr.microsoft.com/azureml/intelmpi2018.3-ubuntu16.04` by default. |

#### CondaSection

| Name                  | Type              | Required | Description                                                  |
| --------------------- | ----------------- | -------- | ------------------------------------------------------------ |
| conda_dependencies_file | String            | No       | The path to the conda dependencies file to use for this run. If a project contains multiple programs with different sets of dependencies, it may be convenient to manage those environments with separate files. The default is None. |
| conda_dependencies     | CondaDependencies | No       | Same as `conda_dependencies_file`, but it is specifies the conda dependencies using an inline dictionary rather than a separated file. |
| pip_requirements_file | String | No | The path to the pip requirements file. |

### HDInsight [not ready for use]

This section is used only for HDInsight components.

| Name            | Type         | Required | Description                                                  |
| --------------- | ------------ | -------- | ------------------------------------------------------------ |
| file            | String       | Yes      | File containing the application to execute, can be a python script or a jar file. It's a relative path to the snapshot folder. |
| files           | List<String> | No       | Files to be used in HDInsight session. Specify relative paths to the snapshot folder. |
| className       | String       | No       | Main class name when main file is a jar.                     |
| jars            | List<String> | No       | Jar files to be used in HDInsight session. Specify relative paths to the snapshot folder. |
| pyFiles         | List<String> | No       | Python files to be used in HDInsight session. Specify relative paths to the snapshot folder. |
| archives        | List<String> | No       | Archives to be used in HDInsight session. Specify relative paths to the snapshot folder. |
| args            | List         | No       | Specify the arguments used along with `file`. This list may consist place holders of Inputs and Outputs. See [CLI Argument Place Holders](#cli-argument-place-holders) for details. |

> **Discussion**:
>
> 1. finalize this design.


### Parallel [not ready for use]

This section is used only for parallel components.

| Name        | Type                   | Required | Description                                                  |
| ----------- | ---------------------- | -------- | ------------------------------------------------------------ |
| input_data  | String or List<String> | Yes      | The input(s) provide the data to be split into mini_batches for parallel execution. Specify the name(s) of the corresponding input(s) here. |
| output_data | String                 | Yes      | The output for the summarized result that generated by the user script. Specify the name of the corresponding output here. |
| entry       | String                 | Yes      | The user script to process mini_batches.                     |
| args        | String                 | No       | Specify the arguments used along with `entry`. This list may consist place holders of Inputs and Outputs. See [CLI Argument Place Holders](#cli-argument-place-holders) for details. |

### Data Types

Data Type is a short word or phrase that describes the data type of the Input or Output.

#### Data Types for Inputs/Outputs

Designer allows its user to connect an Output to another component's Input that with the same data type.

Data type for a Input/Output could be an arbitrary string (except `<` and `>`).

Below are list of data types that will be auto registered and can be directly used by user out-of-box.
For other data type names, please create the DataTypes first following guide from https://aka.ms/azureml-sdk-create-data-type.

**Data Types**

| Name                   | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| path                   | A path contains arbitray data.                               |
| AzureMLDataset         | Represents a dataset, passed directly as id in command line. |

**Data Types used by built-in components**

| Name                   | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| AnyDirectory           | Generic directory which stores arbitray data                 |
| DataFrameDirectory     | Represents tabular data, saved in parquet format by default. |
| ModelDirectory         | Represents a trained model. can be in any format or flavor, will have its own spec file to describe the detailed information. |
| ImageDirectory         | Store images and related meta data in the directory.         |
| UntrainedModelDirectory| Represents an untrained model.                                |
| TransformationDirectory| Represents a transform, only for backward compatibility.     |
| AnyFile                | Generic text/binary file.                                    |
| ZipFile                | A Zipped File.                                               |
| CsvFile                | A CSV or TSV format, with or without header, zipped (of a single file) or unzipped. |


#### Data Types for Parameters

| Name    | Description                                                  |
| ------- | ------------------------------------------------------------ |
| String  | Indicates that the input value is a string.                  |
| Integer | Indicates that the input value is an integer.                |
| Float   | Indicates that the input value is a float.                   |
| Boolean | Indicates that the input value is a boolean value.           |
| Enum    | Indicates that the input value is a enumerated (limited list of) String values. |

### Apendix: Schemas for All kinds of Component

[CommandComponent] (https://github.com/Azure/azureml_run_specification/blob/master/schemas/CommandComponent.yaml)