import numpy as np 
import pandas as pd 
import xgboost as xg 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error as MSE 

# Load the data 

X, y = dataset.iloc[:, :-1], dataset.iloc[:, -1] 

# Splitting 
train_X, test_X, train_y, test_y = train_test_split(X, y, 
					test_size = 0.3, random_state = 123) 

# Instantiation 
xgb_r = xg.XGBRegressor(objective ='reg:linear', 
				n_estimators = 10, seed = 123) 

# Fitting the model 
xgb_r.fit(train_X, train_y) 

# Predict the model 
pred = xgb_r.predict(test_X) 

# RMSE Computation 
rmse = np.sqrt(MSE(test_y, pred)) 
print("RMSE : % f" %(rmse)) 