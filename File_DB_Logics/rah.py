import pandas as pd
from sqlalchemy import create_engine

# Read data from CSV file
df = pd.read_csv("media/files/test.csv")

# Extract columns and data types
cols = list(df.columns)
print(cols)
types = {col: str(df[col].dtype) for col in cols}

print(types)

# Create a connection to the MySQL database
engine = create_engine('mysql://rahul:solver@127.0.0.1:3306/django_mysql')
 

# Create a table in the database
table_name = "my_table"
df.to_sql(table_name, engine, index=False, dtype=types, if_exists='replace')

# Retrieve data from the table
df_new = pd.read_sql(table_name, engine)
print(df)


