import pandas as pd
import pymysql

# Open a connection to the MySQL database
# conn = MySQLdb.connect(host='localhost', user='root', passwd='password', db='django_mysql',)
dbConnection = pymysql.connect(
        host='localhost',
        user='rahul', 
        password = "solver",
        db='django_mysql',
        )
Cursor = dbConnection.cursor()

# Read the CSV file using pandas
df = pd.read_csv('housing.csv')

# Get the data type of each column
data_types = df.dtypes
print(data_types)

# Map pandas data types to MySQL data types
type_map = {
    'int64': 'INT',
    'float64': 'FLOAT',
    'datetime64[ns]': 'DATETIME',
    'object': 'TEXT'
}


# Iterate over the columns and create a MySQL table
# create_query = "CREATE TABLE csv_pandas_kell_etl ("
# for column, data_type in data_types.iteritems():
#     mysql_type = type_map[str(data_type)]
#     create_query += f"{column} {mysql_type},"
# create_query = create_query[:-1] + ")"
# Cursor.execute(create_query)

create_query = "CREATE TABLE csv_housing_kell_etl ("
for column, data_type in data_types.iteritems():
    mysql_type = type_map[str(data_type)]
    create_query += f"`{column}` {mysql_type},"
create_query = create_query[:-1] + ")"
Cursor.execute(create_query)

# Insert data into MySQL table
# for row in df.itertuples():
#     insert_query = f"INSERT INTO csv_pandas_kell_etl VALUES ({','.join([f'{repr(x)}' for x in row[1:]])})"
#     Cursor.execute(insert_query)
for row in df.itertuples():
    values = [repr(x) if str(x) != 'nan' else 'NULL' for x in row[1:]]
    insert_query = f"INSERT INTO csv_housing_kell_etl VALUES ({','.join(values)})"
    Cursor.execute(insert_query)
# Commit changes and close database connection
dbConnection.commit()
dbConnection.close()
