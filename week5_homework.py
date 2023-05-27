# common
import numpy as np
import pandas as pd
import statsmodels.api as sm

# URL
url = ""

def homework(path_winequality_data, X_column, Y_column):
    df = pd.read_csv(path_winequality_data, sep=';')
    X = df[[X_column]]
    Y = df[Y_column]
    X = sm.add_constant(X)
    model = sm.OLS(Y, X)
    result = model.fit()
    my_result = result.rsquared
    return my_result