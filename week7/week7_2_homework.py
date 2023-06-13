import sqlite3
import csv

# SQLite3ファイルに接続
connection = sqlite3.connect('data.sqlite3')
cursor = connection.cursor()

# 2. dataテーブルとgoodsテーブルをgoods_idをキーとして結合してresultテーブルを作成するクエリを実行
query = '''
CREATE TABLE result AS
SELECT data.*, goods.goods_genre_id
FROM data
JOIN goods ON data.goods_id = goods.goods_id
'''
cursor.execute(query)

# 3. resultテーブルのgoods_genre_idごとにpriceの平均値を求めてresult_1テーブルを作成するクエリを実行
query = '''
CREATE TABLE result_1 AS
SELECT goods_genre_id, AVG(price) AS average_price
FROM result
GROUP BY goods_genre_id
'''
cursor.execute(query)

# 4. result_1テーブルをresult.csvに書き出す
query = '''
SELECT * FROM result_1
'''
cursor.execute(query)
result_1 = cursor.fetchall()

with open('result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['goods_genre_id', 'avg_price'])  # ヘッダーを書き出す
    writer.writerows(result_1)  # 結果を書き出す

# 接続を閉じる
cursor.close()
connection.close()
