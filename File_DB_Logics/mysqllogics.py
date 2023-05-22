import csv
import pymysql

# conn = pymysql.connect(host='localhost', user='your_username', password='your_password', db='your_database')
conn = pymysql.connect(host='localhost',user='rahul',password = "solver",db='django_mysql',)

with open('My_People.csv','r') as file:
    reader = csv.reader(file)
    columns = next(reader)
    column_types = []
    for row in reader:
        for col, value in enumerate(row):
            if col >= len(column_types):
                column_types.append('VARCHAR(255)')
            try:
                int(value)
                column_type = 'INT'
            except ValueError:
                try:
                    float(value)
                    column_type = 'FLOAT'
                except ValueError:
                    column_type = 'VARCHAR(255)'
            if column_type == 'INT' and 'VARCHAR' in column_types[col]:
                column_types[col] = 'INT'
            elif column_type == 'FLOAT' and 'VARCHAR' in column_types[col]:
                column_types[col] = 'FLOAT'
    table_name = 'mypeople_csv_table'
    columns_and_types = ', '.join([f'`{column}` {column_type}' for column, column_type in zip(columns, column_types)])
    create_table_sql = f'CREATE TABLE `{table_name}` ({columns_and_types})'
    with conn.cursor() as cursor:
        cursor.execute(create_table_sql)
        
        conn.commit()
print(columns)
print()
print(column_types)