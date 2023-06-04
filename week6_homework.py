# common
import pandas as pd
import numpy as np

## init part(データの読み込みと前処理)
file_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
online_retail_data = pd.ExcelFile(file_url)
online_retail_data_table = online_retail_data.parse('Online Retail')

online_retail_data_table['cancel_flg'] = online_retail_data_table.InvoiceNo.map(lambda x:str(x)[0])
online_retail_data_table["StockCode"] = online_retail_data_table["StockCode"].astype(str) 

# 数字があるものとIDがNullでないものが対象
target_online_retail_data_tb = online_retail_data_table[(online_retail_data_table.cancel_flg == '5') 
                                                        & (online_retail_data_table.CustomerID.notnull())]

target_online_retail_data_tb = target_online_retail_data_tb.assign(TotalPrice=target_online_retail_data_tb.Quantity * target_online_retail_data_tb.UnitPrice)

# working place. everything 
def homework(target_online_retail_data_tb):
    my_result = 0
    return my_result

def homework(target_online_retail_data_tb):
    trans_a = set(target_online_retail_data_tb[target_online_retail_data_tb['StockCode'] == '20725'].InvoiceNo)
    trans_b = set(target_online_retail_data_tb[target_online_retail_data_tb['StockCode'] == '22383'].InvoiceNo)
    trans_ab = trans_a & trans_b
    trans_all = set(target_online_retail_data_tb.InvoiceNo)
    support_b = len(trans_b) / len(trans_all)
    confidence = len(trans_ab) / len(trans_a)
    my_result = confidence / support_b
    return my_result