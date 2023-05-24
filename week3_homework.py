# import
import numpy as np
import pandas as pd
from pandas import DataFrame
# add url
url_winequality_data = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
# my function
def homework(url_winequality_data, n):
    import requests
    import io
    r = requests.get(url_winequality_data)
    winequality_red_table = pd.read_csv(io.StringIO(r.text), sep=';')
    volatile_acidity = winequality_red_table['volatile acidity']
    volatile_acidity_cut = pd.qcut(volatile_acidity, q=n, duplicates='drop')
    winequality_red_table['volatile_acidity_cut'] = volatile_acidity_cut
    my_result = winequality_red_table[winequality_red_table['quality'] == 5].groupby('volatile_acidity_cut')['alcohol'].mean().min()
    return my_result