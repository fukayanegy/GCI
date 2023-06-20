import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

# データの読み取り
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# 欠損値の確認
print(train_data.isnull().sum())
print(test_data.isnull().sum())

# 目的変数の分布
sns.countplot(data=train_data, x="TARGET")
plt.show()
