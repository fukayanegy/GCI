import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns

test_path = "test.csv"
data = pd.read_csv("train.csv")
# Check the missing values for each item
print(data.isnull().sum())
# Delete 'Cabin' due to many missing values
data.drop('Cabin', axis = 1, inplace = True)
# For the missing value of age or embarke, we will remove the row itself for now
data = data.dropna()
# 欠損値のないデータは712になった
print(len(data))
# カテゴリカル・データを質的変数に置き換える
# Age を male = 0, female = 1 に置き換える
data.replace({'Sex': {'male': 0, 'female': 1}}, inplace = True)
# Embarked を S = 0, C = 1, Q = 2 に置き換える
data.replace({'Embarked': {'S': 0, 'C': 1, 'Q': 2}}, inplace = True)
print(data.head())