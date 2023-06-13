import sqlite3
import csv

# SQLite3ファイルに接続
connection = sqlite3.connect('data.sqlite3')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS result')
cursor.execute('DROP TABLE IF EXISTS result_1')

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

# 4. result_1テーブルをresult.csvに書き出す（goods_genre_idの欠損を補完し、priceの欠損値は0とする）
query_3 = '''
SELECT goods_genre_id, IFNULL(average_price, 0) AS average_price
FROM (
    SELECT g.goods_genre_id, r.average_price
    FROM (
        SELECT goods_genre_id
        FROM goods
        UNION
        SELECT DISTINCT goods_genre_id
        FROM result_1
    ) g
    LEFT JOIN result_1 r ON g.goods_genre_id = r.goods_denre_id
)
ORDER BY goods_genre_id
'''
cursor.execute(query_3)
result_1 = cursor.fetchall()

with open('result.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['goods_genre_id', 'average_price'])  # ヘッダーを書き出す
        writer.writerows(result_1)  # 結果を書き出す

# 接続を閉じる
cursor.close()
connection.close()
