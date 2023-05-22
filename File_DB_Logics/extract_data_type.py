import csv
import pymysql

# conn = pymysql.connect(host='localhost', user='your_username', password='your_password', db='your_database')
conn = pymysql.connect(host='localhost',user='rahul',password = "solver",db='django_mysql',)



with open('My_People.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    
column_names = data[0]
# modify column names to enclose them in backticks
column_names = [f"`{column}`" for column in column_names]
table_name = 'mypeople_csv_table'
sql = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['%s' for _ in column_names])})"

with conn.cursor() as cursor:
    for row in data[1:]:
        cursor.execute(sql,row)
    conn.commit()


# with open('My_People.csv','r') as file:
#     reader = csv.reader(file)
#     columns = next(reader)
#     column_types = []
#     for row in reader:
#         for col, value in enumerate(row):
#             if col >= len(column_types):
#                 column_types.append('VARCHAR(255)')
#             try:
#                 int(value)
#                 column_type = 'INT'
#             except ValueError:
#                 try:
#                     float(value)
#                     column_type = 'FLOAT'
#                 except ValueError:
#                     column_type = 'VARCHAR(255)'
#             if column_type == 'INT' and 'VARCHAR' in column_types[col]:
#                 column_types[col] = 'INT'
#             elif column_type == 'FLOAT' and 'VARCHAR' in column_types[col]:
#                 column_types[col] = 'FLOAT'
                

# with open('My_People.csv','r') as file:
#     #reader = csv.reader(file)
#     reader = csv.DictReader(file)
#     data = [row for row in reader]
# print(data)
# print(columns)     
# print(column_types)


# table_name="hog_csv_table"
# table_name = 'mypeople_csv_table'
# #table_name = 'olympics_csv_table'
# # sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in columns])})"

# # with conn.cursor() as cursor:
# #     for row in data[1:]:
        
# #         cursor.execute(sql, row)
# #     conn.commit()


# # Insert the data from the CSV file into the new table
# insert_query = 'INSERT INTO {} ({}) VALUES ({})'.format(
#     table_name,
#     ', '.join(data[0].keys()),
#     ', '.join(['%s'] * len(data[0]))
# )
# with conn.cursor() as cursor:
#     for row in data:
#         cursor.execute(insert_query, tuple(row.values()))
#     conn.commit()
# cursor=conn.cursor()
# for row in data:
#     cursor.execute(insert_query, tuple(row.values()))

# # Commit the changes to the database and close the connection
# conn.commit()
# cursor.close()
# conn.close()


