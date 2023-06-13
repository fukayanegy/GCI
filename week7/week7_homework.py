import sqlite3
import csv

# SQLite3ファイルに接続
connection = sqlite3.connect('data.sqlite3')
cursor = connection.cursor()

# 1. dataテーブルとgoodsテーブルをgoods_idをキーとして結合するクエリを実行
query = '''
SELECT data.goods_id, goods.goods_genre_id, data.price
FROM data
JOIN goods ON data.goods_id = goods.goods_id
'''
cursor.execute(query)
result = cursor.fetchall()

query_2 = '''
select goods_denre_id, AVG(price) as averge_price
from result
group by goods_denre_id
'''

cursor.execute(query_2)
result_2 = cursor.fetchall()

# 接続を閉じる
cursor.close()
connection.close()