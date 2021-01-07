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
parser = argparse.ArgumentParser("XGBRegressorTraining")
parser.add_argument("--Training_Data", type=str, help="Training dataset")
parser.add_argument("--Lable_Col", type=str, help="Lable column in the dataset.")
parser.add_argument("--Learning_rate", type=float, help="Boosting learning rate.")
parser.add_argument("--Max_depth", type=int, help="Maximum tree depth for base learners.")
parser.add_argument("--Model_FileName", type=str, help="Name of the model file.")
parser.add_argument("--Model_Path", type=str, help="Path to store XGBoost model file in Json format.")
args = parser.parse_args()

## Load data from DataFrameDirectory to Pandas DataFrame
training_df = load_data_frame_from_directory(args.Training_Data).data

## Prepare training data
training_df_features = training_df[[c for c in training_df.columns if c!=args.Lable_Col]]
training_df_lable = training_df[args.Lable_Col]

## Training
xg_reg = xgb.XGBRegressor(
                objective ='reg:linear', colsample_bytree = 0.3, alpha = 10, n_estimators = 10,
                learning_rate = args.Learning_rate,
                max_depth = args.Max_depth
)

xg_reg.fit(training_df_features, training_df_lable)

## Output model
os.makedirs(args.Model_Path, exist_ok=True)
xg_reg.save_model(args.Model_Path + "/" + args.Model_FileName)
