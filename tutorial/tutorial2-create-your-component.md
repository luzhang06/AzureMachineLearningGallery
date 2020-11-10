# Tutorial 2: Create your own component

In [tutorial 1](./tutorial1-use-existing-components.md), you learned how to use existing components in the gallery. What if the component you want is not in the gallery? You can create your own component and share it in the gallery with others. This tutorial will walk through how to create your own component.

This tutorial will continue to use the NYC Taxi Fare Prediction pipeline in tutorial 1. In tutorial 1, we already build a pipeline to train a XGBoost model. Now let's add one more data processing component before train the model. 

The script and YAML spec of components used in tutorial 1 is available under */components/nyc-taxi-fare-prediction* folder, please go through the YAML spec and script to have an overview how the YAML spec works. 

Basically, it's possible to wrap arbitrary code as Azure Machine Learning component by following the component specification. A component specification in YAML format describes the component in the Azure Machine Learning system. A component definition has the following parts:

- **Metadata:** name, description, etc.
- **Interface:**: input/output specifications (name, type, description, default value, etc).
- **Implementation:**: A specification of how to run the component given a set of argument values for the component’s inputs, including source code and environment required to run the component. 

Refer to [component spec definition](../component-spec-definition.md) for more details. 

Now let's add a component to Normalize the nyc data before train a model. Following scripts will be used to do the normalization. It will replace undefined values, change column type and split the datetime column to date and time. 

```dotnetcli
import argparse
import os
import pandas as pd
from azureml.studio.core.io.data_frame_directory import load_data_frame_from_directory, save_data_frame_to_directory

print("Replace undefined values to relavant values and rename columns to meaningful names")

parser = argparse.ArgumentParser("normalize")
parser.add_argument("--merged_data", type=str, help="merged taxi data")
parser.add_argument("--output_normalize", type=str, help="replaced undefined values and renamed columns")

args = parser.parse_args()
combined_converted_df = load_data_frame_from_directory(args.filtered_data).data
print("Argument (output normalized taxi data path): %s" % args.output_normalize)

# These functions replace undefined values and rename to use meaningful names.
replaced_stfor_vals_df = (combined_converted_df.replace({"store_forward": "0"}, {"store_forward": "N"})
                          .fillna({"store_forward": "N"}))

replaced_distance_vals_df = (replaced_stfor_vals_df.replace({"distance": ".00"}, {"distance": 0})
                             .fillna({"distance": 0}))

normalized_df = replaced_distance_vals_df.astype({"distance": 'float64'})

temp = pd.DatetimeIndex(normalized_df["pickup_datetime"])
normalized_df["pickup_date"] = temp.date
normalized_df["pickup_time"] = temp.time

temp = pd.DatetimeIndex(normalized_df["dropoff_datetime"])
normalized_df["dropoff_date"] = temp.date
normalized_df["dropoff_time"] = temp.time

del normalized_df["pickup_datetime"]
del normalized_df["dropoff_datetime"]

normalized_df.reset_index(inplace=True, drop=True)

if not (args.output_normalize is None):
    os.makedirs(args.output_normalize, exist_ok=True)
    print("%s created" % args.output_normalize)
    save_data_frame_to_directory(args.output_normalize, normalized_df)
``` 


Now please write the YAML spec to wrap above script as a component. You can refer the YAML spec under /components/nyc-taxi-fare-prediction. 

After write up the YAML spec, please register it to your workspace and add the component in the NYC Taxi Fare Prediction pipeline we build in tutorial 1.  