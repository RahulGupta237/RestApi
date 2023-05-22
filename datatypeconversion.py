import pandas as pd

# define a dictionary that maps Pandas data types to MySQL data types
data_types = {
    'int64': 'INT',
    'float64': 'FLOAT',
    'datetime64': 'DATETIME',
    'object': 'VARCHAR(255)',
    'bool': 'BOOL',
    'category': 'VARCHAR(255)'
}

# read the CSV file into a Pandas dataframe
df = pd.read_csv('filename.csv')

# get the data type of the column
col_data_type = df['column_name'].dtype

# convert the Pandas data type to the MySQL data type
mysql_data_type = data_types[str(col_data_type)]

# print the MySQL data type
print(f"MySQL data type: {mysql_data_type}")
