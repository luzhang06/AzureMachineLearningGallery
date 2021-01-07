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
parser = argparse.ArgumentParser("XGBRegressorEvaluation")
parser.add_argument("--Evaluation_Data", type=str, help="Evaluation dataset.")
parser.add_argument("--Lable_Col", type=str, help="Lable column in the evaluation dataset.")
parser.add_argument("--Model_Path", type=str, help="Path where contains model file.")
parser.add_argument("--Model_FileName", type=str, help="Name of the model file.")
parser.add_argument("--Evaluation_Output", type=str, help="Evaluation result")
args = parser.parse_args()

## Load data from DataFrameDirectory to Pandas DataFrame
evaluation_df = load_data_frame_from_directory(args.Evaluation_Data).data

## Prepare evaluation data
evaluation_df_features = evaluation_df[[c for c in evaluation_df.columns if c!=args.Lable_Col]]
evaluation_df_lable = evaluation_df[args.Lable_Col]

## Load model
xg_reg = xgb.XGBRegressor()
xg_reg.load_model(args.Model_Path + "/" + args.Model_FileName)

## Evaluation
preds = xg_reg.predict(evaluation_df_features)
rmse = np.sqrt(mean_squared_error(evaluation_df_lable, preds))
print("RMSE: %f" % (rmse))

## Output evaluation result
evaluation_result_df = pd.DataFrame(np.array([rmse]), columns=['RMSE Result'])
os.makedirs(args.Evaluation_Output, exist_ok=True)
save_data_frame_to_directory(args.Evaluation_Output, evaluation_result_df)
