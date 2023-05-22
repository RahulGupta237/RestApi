import csv

with open('My_People.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

print("Data of CSV")
print("*******************************************")

#data = [[i for i in item if i != ''] for item in data]
# c = [item for item in b if item != []]
print(data)
column_names = data[0]

print()
print()
#column_names=[i for i in column_names if i]
print(column_names)
print()

print("extract data type from csv")

column_data_types = []

for i in range(len(column_names)):
    column_data_type = 'VARCHAR(255)' # default data type is VARCHAR(255)
    
    for j in range(1, len(data)):
        try:
            int(data[j][i])
            column_data_type = 'INT'
        except ValueError:
            try:
                float(data[j][i])
                column_data_type = 'FLOAT'
            except ValueError:
                pass
            
        column_data_types.append(column_data_type)
print()
print(column_data_types)

import pymysql

conn = pymysql.connect(host='localhost',user='rahul',password = "solver",db='django_mysql',)

table_name="MyData"
sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{column_names[i]} {column_data_types[i]}' for i in range(len(column_names))])})"

# Insert the data from the CSV file into the new table
insert_query = 'INSERT INTO {} ({}) VALUES ({})'.format(
    table_name,
    ', '.join(data[0][::]),
    ', '.join(['%s'] * len(data[0]))
)


with conn.cursor() as cursor:
    cursor.execute(sql)
    conn.commit()

with conn.cursor() as cursor:
    try:
            table_created=True
            cursor.execute(sql)
          
            print("table successfully created")
    except:
        pass
        print("something went wrong",table_created)

    try:
        insert=False
        for row in data:
            insert=True
            cursor.execute(insert_query, tuple(row.values()))
    except:
        pass
        print("i am danger")
    finally:
          print(f"successfully inserted {insert}")
          conn.commit()
          conn.close()




        


        
    


