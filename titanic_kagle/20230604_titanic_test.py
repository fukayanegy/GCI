import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree

data = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
# Check the missing values for each item
# Delete 'Cabin' due to many missing values
data.drop('Cabin', axis = 1, inplace = True)
test.drop('Cabin', axis = 1, inplace = True)
# For the missing value of age or embarke, we will remove the row itself for now
# data = data.dropna()
# test = test.dropna()
data['Age'] = data['Age'].fillna(0)
test['Age'] = test['Age'].fillna(0)
# 欠損値のないデータは712になった

# nameを分ける
data_name_sep = data['Name'].str.split('[,.]', expand=True)
test_name_sep = test['Name'].str.split('[,.]', expand=True)
data_name_sep.drop(3, axis=1, inplace=True)
data[['Firstname', 'Title', 'Familyname']] = data_name_sep
test[['Firstname', 'Title', 'Familyname']] = test_name_sep


# カテゴリカル・データを質的変数に置き換える
# Age を male = 0, female = 1 に置き換える
data.replace({'Sex': {'male': 0, 'female': 1}}, inplace = True)
test.replace({'Sex': {'male': 0, 'female': 1}}, inplace = True)
# Embarked を S = 0, C = 1, Q = 2 に置き換える
data.replace({'Embarked': {'S': 0, 'C': 1, 'Q': 2}}, inplace = True)
test.replace({'Embarked': {'S': 0, 'C': 1, 'Q': 2}}, inplace = True)
# # カテゴリカル・データを質的変数に置き換える
# # Age を male = 0, female = 1 に置き換える
# data_sex_dummy = pd.get_dummies(data['Sex'])
# data = pd.concat([data, data_sex_dummy], axis=1)
# test_sex_dummy = pd.get_dummies(test['Sex'])
# test = pd.concat([test, test_sex_dummy], axis=1)
# # Embarked を S = 0, C = 1, Q = 2 に置き換える
# data_embarked_dummy = pd.get_dummies(data['Embarked'])
# data = pd.concat([data, data_embarked_dummy], axis=1)
# data_embarked_dummy = pd.get_dummies(test['Embarked'])
# test = pd.concat([test, data_embarked_dummy], axis=1)
# # 敬称を数値に置き換える
# data_Title_dummy = pd.get_dummies(data['Title'])
# data = pd.concat([data, data_Title_dummy], axis=1)
# test_Title_dummy = pd.get_dummies(test['Title'])
# test = pd.concat([data, test_Title_dummy], axis=1)
# 使うcolumnを説明変数と非説明変数に置き換える
# target = data["Perished"].values
# feature_one = data[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Title"]]
# my_tree = tree.DecisionTreeClassifier()
# my_tree = my_tree.fit(feature_one, target)
# test_feature = test[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]].values
# my_result = my_tree.predict(test_feature)
# result_ID = np.array(test["PassengerId"]).astype(int)
# data = {'PassengerId': result_ID, 'Survived': my_result}
# df = pd.DataFrame(data)
# df.to_csv('submission.csv', index=False)
data.to_csv('data_re.csv', index=False)