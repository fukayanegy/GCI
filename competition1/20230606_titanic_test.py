import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame, Series
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV



data = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# 欠損値を埋める作業
## Cabin 変数を消す
data.drop('Cabin', axis = 1, inplace = True)
test.drop('Cabin', axis = 1, inplace = True)
## Age Fareを平均値で埋める
age = pd.concat([data['Age'], test['Age']])
fare = pd.concat([data['Fare'], test['Fare']])
data['Age'].fillna(age.mean(), inplace=True)
test['Age'].fillna(age.mean(), inplace=True)
data['Fare'].fillna(fare.mean(), inplace=True)
test['Fare'].fillna(fare.mean(), inplace=True)
## Embarked をSで埋める
data['Embarked'].fillna('S', inplace=True)
test['Embarked'].fillna('S', inplace=True)

data_dummy = data
test_dummy = test


# nameを分ける
data_name_sep = data['Name'].str.split('[,.]', expand=True)
test_name_sep = test['Name'].str.split('[,.]', expand=True)
data_name_sep.drop(3, axis=1, inplace=True)
data[['Firstname', 'Title', 'Familyname']] = data_name_sep
test[['Firstname', 'Title', 'Familyname']] = test_name_sep
data.drop('Name', axis=1, inplace=True)
test.drop('Name', axis=1, inplace=True)


# Title を分ける
data['Title'] = data['Title'].where(data['Title'].isin([' Master', ' Miss', ' Mr', ' Mrs', ' Dr', ' Rev']), 'others')
test['Title'] = test['Title'].where(test['Title'].isin([' Master', ' Miss', ' Mr', ' Mrs', ' Dr', ' Rev']), 'others')


# dummy変数の作成
## Sex のdummy変数作成
data_dummy = pd.get_dummies(data_dummy, columns=['Sex'])
test_dummy = pd.get_dummies(test_dummy, columns=['Sex'])

## Title のdummy変数作成
data_dummy = pd.get_dummies(data_dummy, columns=['Title'])
test_dummy = pd.get_dummies(test_dummy, columns=['Title'])

## Embarked のdummy変数作成
data_dummy = pd.get_dummies(data_dummy, columns=['Embarked'])
test_dummy = pd.get_dummies(test_dummy, columns=['Embarked'])

print(test_dummy.columns)
target = data_dummy["Perished"].values
feature_one = data_dummy[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_female', 'Sex_male', 'Title_ Dr', 'Title_ Master', 'Title_ Miss', 'Title_ Mr', 'Title_ Mrs', 'Title_ Rev', 'Title_others', 'Embarked_C', 'Embarked_Q', 'Embarked_S']]
my_tree = tree.DecisionTreeClassifier()
my_tree = my_tree.fit(feature_one, target)
test_feature = test_dummy[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_female', 'Sex_male', 'Title_ Dr', 'Title_ Master', 'Title_ Miss', 'Title_ Mr', 'Title_ Mrs', 'Title_ Rev', 'Title_others', 'Embarked_C', 'Embarked_Q', 'Embarked_S']].values
my_result = my_tree.predict(test_feature).astype(str)
result_ID = np.array(test["PassengerId"])
data = {'PassengerId': result_ID, 'Perished': my_result}
df = pd.DataFrame(data)
df.to_csv('submission.csv', index=False)
