import csv
import pymysql

conn = pymysql.connect(host='localhost',user='rahul',password = "solver",db='django_mysql',)

with open('housing.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    
column_names = data[0]
column_names = [f"`{column}`" for column in column_names]
table="hog_csv_table"
sql = f"INSERT INTO {table} ({', '.join(column_names)}) VALUES ({', '.join(['%s' for _ in column_names])})"

with conn.cursor() as cursor:
    for row in data[1:]:
        cursor.execute(sql, row)
    conn.commit()
