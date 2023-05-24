# common
import pandas as pd
import numpy as np

# init part(データの読み込みと前処理)
file_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
online_retail_data = pd.ExcelFile(file_url)
online_retail_data_table = online_retail_data.parse('Online Retail')

# 採点の都合上、文字列型に変換
online_retail_data_table['cancel_flg'] = online_retail_data_table.InvoiceNo.map(lambda x:str(x)[0])

# InvoiceNoの先頭が5であるものとIDがNullでないものが対象
target_online_retail_data_tb = online_retail_data_table[(online_retail_data_table.cancel_flg == '5') 
                                                        & (online_retail_data_table.CustomerID.notnull())]

target_online_retail_data_tb = target_online_retail_data_tb.assign(TotalPrice=target_online_retail_data_tb.Quantity * target_online_retail_data_tb.UnitPrice)

def homework(target_online_retail_data_tb, n):
    customer_total_price = target_online_retail_data_tb.groupby('CustomerID')['TotalPrice'].sum()
    customer_total_price_sort_values = customer_total_price.sort_values(ascending=False)
    customer_len = len(customer_total_price_sort_values)
    group_count = min(customer_len, n)
    customers_qcut = pd.qcut(customer_total_price_sort_values, q=group_count, labels=False)
    grouped_total_price = customer_total_price_sort_values.groupby(customers_qcut).sum()
    grouped_percentage = grouped_total_price / grouped_total_price.sum()
    my_result = pd.Series(grouped_percentage.sort_values(ascending=False), name='グループ')
    return my_result