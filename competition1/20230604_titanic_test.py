import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree

data = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
data.drop('Cabin', axis = 1, inplace = True)
test.drop('Cabin', axis = 1, inplace = True)
age = pd.concat([data['Age'], test['Age']])
fare = pd.concat([data['Fare'], test['Fare']])
data['Age'].fillna(age.mean(), inplace=True)
test['Age'].fillna(age.mean(), inplace=True)
data['Fare'].fillna(fare.mean(), inplace=True)
test['Fare'].fillna(fare.mean(), inplace=True)
data['Embarked'].fillna('S', inplace=True)
test['Embarked'].fillna('S', inplace=True)

# カテゴリカル・データを質的変数に置き換える
# Age を male = 0, female = 1 に置き換える
data.replace({'Sex': {'male': 0, 'female': 1}}, inplace = True)
test.replace({'Sex': {'male': 0, 'female': 1}}, inplace = True)

# Embarked を S = 0, C = 1, Q = 2 に置き換える
data.replace({'Embarked': {'S': 0, 'C': 1, 'Q': 2}}, inplace = True)
test.replace({'Embarked': {'S': 0, 'C': 1, 'Q': 2}}, inplace = True)

# 使うcolumnを説明変数と非説明変数に置き換える
target = data["Perished"].values
feature_one = data[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]]
my_tree = tree.DecisionTreeClassifier()
my_tree = my_tree.fit(feature_one, target)
test_feature = test[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]].values
my_result = my_tree.predict(test_feature)
result_ID = np.array(test["PassengerId"]).astype(int)
data = {'PassengerId': result_ID, 'Survived': my_result}
df = pd.DataFrame(data)
df.to_csv('submission.csv', index=False)