import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import xgboost as xgb
import category_encoders as ce
from sklearn.model_selection import train_test_split

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# missing values check
print(train_data.isnull().sum())
print(test_data.isnull().sum())

# make up for missing values
