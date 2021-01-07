import os
import pandas as pd
import pathlib

def read_as_dataframe(input_path: str):
    if os.path.isfile(input_path):
        if input_path.endswith(".csv"):
            return pd.read_csv(input_path)
        elif input_path.endswith(".parquet"):
            return pd.read_parquet(input_path)
    else:
        dir_path = pathlib.Path(input_path)

        csv_files = list(dir_path.glob("**/*.csv"))
        if csv_files:
            df_from_csv_files = (pd.read_csv(f) for f in csv_files)
            return pd.concat(df_from_csv_files, ignore_index=True)

        parquet_files = list(dir_path.glob("**/*.parquet"))
        if parquet_files:
            df_from_parquet_files = (pd.read_parquet(f) for f in parquet_files)
            return pd.concat(df_from_parquet_files, ignore_index=True)

    raise ValueError(f"Failed to read path: {input_path}")