import csv
import pymysql

# Open a connection to the MySQL database
# conn = MySQLdb.connect(host='localhost', user='root', passwd='password', db='django_mysql',)
dbConnection = pymysql.connect(
        host='localhost',
        user='rahul', 
        password = "solver",
        db='django_mysql',
        )
cursor = dbConnection.cursor()

# Read the CSV file into a list of dictionaries
with open('test.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]
    

# Create a table based on the column headers in the CSV file
table_name = 'csv_table'
create_table_query = 'CREATE TABLE IF NOT EXISTS {} ({})'.format(
    table_name,
    ', '.join(['{} VARCHAR(255)'.format(key) for key in data[0].keys()])
)
cursor.execute(create_table_query)

# Insert the data from the CSV file into the new table
insert_query = 'INSERT INTO {} ({}) VALUES ({})'.format(
    table_name,
    ', '.join(data[0].keys()),
    ', '.join(['%s'] * len(data[0]))
)

for row in data[1::]:
    cursor.execute(insert_query, tuple(row.values()))

# Commit the changes to the database and close the connection
dbConnection.commit()
cursor.close()
dbConnection.close()
