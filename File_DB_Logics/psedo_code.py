# Import necessary libraries
import mysql.connector

# Define connection to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="rahul",
    password="solver",
    database="django_mysql"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Open the file and read the contents
with open("media/files/test.txt", "r") as f:
    # Read the first line to get the column headers
    headers = f.readline().split(",")

    # Read the rest of the lines to get the data
    data = []
    for line in f.readlines():
        data.append(line.strip().split(","))

# Extract the column and data types
column_types = {}
for i in range(len(headers)):
    column = headers[i]
    data_type = type(data[0][i]).__name__
    column_types[column] = data_type

# Create a table based on the column and data types
table_name = "mytable"
query = f"CREATE TABLE {table_name} ("
for column, data_type in column_types.items():
    query += f"{column} {data_type}, "
query = query[:-2] + ")"
cursor.execute(query)

# Insert the data into the table
query = f"INSERT INTO {table_name} ("
for column in headers:
    query += f"{column}, "
query = query[:-2] + ") VALUES ("
for row in data:
    for value in row:
        query += f"'{value}', "
    query = query[:-2] + "), ("
query = query[:-3]
cursor.execute(query)
db.commit()

# Retrieve data from the table
query = f"SELECT * FROM {table_name}"
cursor.execute(query)
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)
