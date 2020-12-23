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
| metadata            | [MetaData](#MetaData)                                    | No       | A metadata structure to store additional information for the component, like tags. |
| tags                | Dictionary<String>                                       | No | A list of tags to describe the category of the component. Each tag should be one word or a short phrase to describe the component, e.g. `Office`, `NLP`, `ImageClassification`. |
| is_deterministic    | Boolean                                                  | No       | Specify whether the component will always generate the same result when given the same input data. Defaults to `True` if not specified. Typically for components which will load data from external resources, e.g. Import data from a given url, should set to `False` since the data to where the url points to may be updated. |
| inputs              | Dictionary<String, [Input](#Input) or [Parameter](#Parameter)> | No       | Defines input ports and parameters of the component. The string key is the name of Input/Parameter, which should be a valid python variable name. |
| outputs             | Dictionary<String, [Output](#Output)>                    | No       | Defines output ports of the component. The string key is the name of Output, which should be a valid python variable name. |
| code                | String                                                   | No       | Location of the [Code](#Code) snapshot. |
| environment         | [Environment](#Environment)                              | No       | An Environment defines the runtime environment for the component to run. Refer to [here](component-spec-topics/running-environment.md) for details. |
| command             | List<String>                                             | Yes      | Specify the command to start to run the component code.         |

#### Name

Our recommendation to the component name will be something like `company`.`team`.`name-of-component`.

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

#### Code

A code snapshot can be expressed as one of 3 things:

      1. a local file path relative to the file where it is referenced e.g. './code'. Register Only support this form now.
      2. an http url e.g. 'http://github.com/foo/bar/dir#239870234080'
      3. a snapshot id, e.g.: aml://6560575d-fa06-4e7d-95fb-f962e74efd7a/azml-rg/sandbox-ws/snapshots/293lkw0j23fw8cv.

### MetaData

Metadata defines additional information for the component. Currently supported properties are listed below.

| Name        | Type         | Required | Description                                                  |
| ----------- | ------------ | -------- | ------------------------------------------------------------ |
| contact     | String       | No       | The contact info of the component's author. Typically contains user or organization's name and email. e.g. `AzureML Studio Team <stcamlstudiosg@microsoft.com>`. |
| helpDocument | String       | No       | The url of the component's documentation. The url is shown as a link on AzureML Designer's page. |

### Tags
Some predefined tags used by azure-ml-component package.
| Name        | Type         | Required | Description                                                  |
| ----------- | ------------ | -------- | ------------------------------------------------------------ |
| codegenBy | String | No  | The component spec might be generated by some automation tool. Set the tool name into this field. e.g. `dsl.component` |

### Input

Defines an input port of the component. Refer to [here](component-spec-topics/inputs-and-outputs.md) for details.

| Name         | Type                    | Required | Description                                                  |
| ------------ | ----------------------- | -------- | ------------------------------------------------------------ |
| type         | String or  List<String> | Yes      | Defines the data type(s) of this input port. Refer to [Data Types for Inputs/Outputs](#Data Types for Inputs/Outputs) for details. |
| display_name | String                  | No      | Display name of the input port. |
| optional     | Boolean                 | No       | Indicates whether this input is an optional port. Defaults to `False` if not specified. |
| description  | String                  | No       | Detailed description to the input port.      |

### Parameter

Defines a parameter of the component. Refer to [here](component-spec-topics/inputs-and-outputs.md) for details.

| Name         | Type    | Required | Description                                                  |
| ------------ | ------- | -------- | ------------------------------------------------------------ |
| type         | String  | Yes      | Defines the type of this data. Refer to [Data Types for Parameters](#Data Types for Parameters) for details. |
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
| type         | String | Yes      | Defines the data type(s) of this output port. Refer to [Data Types for Ports](#Data Types for Ports) for details. |
| display_name | String | No       | Display name of the parameter.                               |
| description  | String | No       | Detailed description to the output port.                     |


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

### HDInsight

This section is used only for HDInsight components.

| Name            | Type         | Required | Description                                                  |
| --------------- | ------------ | -------- | ------------------------------------------------------------ |
| file            | String       | Yes      | File containing the application to execute, can be a python script or a jar file. It's a relative path to the snapshot folder. |
| files           | List<String> | No       | Files to be used in HDInsight session. Specify relative paths to the snapshot folder. |
| className       | String       | No       | Main class name when main file is a jar.                     |
| jars            | List<String> | No       | Jar files to be used in HDInsight session. Specify relative paths to the snapshot folder. |
| pyFiles         | List<String> | No       | Python files to be used in HDInsight session. Specify relative paths to the snapshot folder. |
| archives        | List<String> | No       | Archives to be used in HDInsight session. Specify relative paths to the snapshot folder. |
| args            | List         | No       | Specify the arguments used along with `file`. This list may consist place holders of Inputs and Outputs. See [CLI Argument Place Holders](#CLI Argument Place Holders) for details. |

> **Discussion**:
>
> 1. finalize this design.


### Parallel

This section is used only for parallel components.

| Name            | Type                              | Required | Description                                                  |
| --------------- | --------------------------------- | -------- | ------------------------------------------------------------ |
| inputData       | String or List<String>            | Yes      | The input(s) provide the data to be split into mini_batches for parallel execution. Specify the name(s) of the corresponding input(s) here. |
| outputData      | String                            | Yes      | The output for the summarized result that generated by the user script. Specify the name of the corresponding output here. |
| entry           | String                            | Yes      | The user script to process mini_batches.                     |

> **Discussion**:
>
> 1. finalize this design.

### Data Types

Data Type is a short word or phrase that describes the data type of the Input or Output.

#### Data Types for Inputs/Outputs

Designer allows its user to connect an Output to another component's Input that with the same data type.

Data type for a Input/Output could be an arbitrary string (except `<` and `>`), but it is strongly recommended to follow `PascalCase` style.

#### Data Types for Parameters

| Name    | Description                                                  |
| ------- | ------------------------------------------------------------ |
| String  | Indicates that the input value is a string.                  |
| Integer | Indicates that the input value is an integer.                |
| Float   | Indicates that the input value is a float.                   |
| Boolean | Indicates that the input value is a boolean value.           |
| Enum    | Indicates that the input value is a enumerated (limited list of) String values. |

### CLI Argument Place Holders

When invoking from a CLI interface, the arguments are specified with placeholders. The placeholders will be replaced with the actual value when running.

Example:

```yaml
command:
- python
- basic_component.py
- [--input_dir, $inputPath: inputs.input_dir]
- [--str_param, $inputValue: inputs.str_param]
- --enum_param
- $inputValue: inputs.enum_param
```

Placeholder is a dictionary that:

* The key may be either `inputValue` for inferring values from Parameters, `inputPath` for inferring values from Input Ports, or `outputPath` for Output Ports.
* The value should be the `name` of Input or Output.

### Apendix: Schemas for All kinds of Component

[CommandComponent] (https://github.com/Azure/azureml_run_specification/blob/master/schemas/CommandComponent.yaml)