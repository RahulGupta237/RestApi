import csv
from collections import Counter

# Define a function to get the data type of a value
def get_data_type(value):
    try:
        float(value)
        return "numeric"
    except ValueError:
        if value.strip() == "":
            return "empty"
        else:
            return "string"

# Read the CSV file
with open('My_People.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Extract the column names from the first row
columns = data[0]
print(columns)
# Loop through each column in the data
column_data={}
data_type={}
null_counts=[]
empty_counts=[]
for i, column in enumerate(columns):
    
    # Print the column name
    print(f"Column name: {column}")
    
    # Extract the values in the column
    values = [row[i] for row in data[1:]]
    print(values)
    column_data[column]=values
    
    # Print the data type of the column
    data_types = [get_data_type(value) for value in values]
    data_type[column]=data_types

    print(f"Data type: {Counter(data_types)}")
    
    # Print the number of null values in the column
    null_count = values.count('')
    if null_count!=0:
       null_counts.append(null_count)
    print(f"Null count: {null_count}")
    
    # Print the number of empty values in the column
    empty_count = data_types.count('empty')
    if empty_count!=0:
        empty_counts.append(empty_counts)
    print(f"Empty count: {empty_count}")
    
    # Print the number of duplicate records in the column
    duplicate_count = len(values) - len(set(values))
    print(f"Duplicate count: {duplicate_count}")
list1=[1,2,3,4]
print(column_data)
print(sum(null_counts))
print(len(empty_counts))
print(data_type)
print(f"***********{sum(list1)}****************")

# data_types = {}
# for column in columns:
#     data_types[column] = None
# rows_data = []
# column_data = {}
# for column in columns:
#     column_data[column] = []
# row_set = set()

# # Create a variable to store the number of null values
# null_count = 0
# empty_count=0
# duplicate_row=[]
# # Iterate over the rows in the CSV file to infer data types and check for null values, empty values, and duplicate values
# for row in data[1]:
#     row_data = {}
#     for column in columns:
#         value = row[column]

#         # Check for null values
#         if value is None:
#             null_count += 1
#             continue
            

#         # Check for empty values
#         if value.strip() == '':
#             empty_count += 1
#             continue

#         # Add the value to the column data list
#         column_data[column].append(value)

#         # Infer data types
#         if not value:
#             continue
#         elif data_types[column] is None:
#             # If the data type has not been inferred yet, try to infer it from the first row
#             if value.isdigit():
#                 data_types[column] = 'integer'
#             elif value.replace('.', '', 1).isdigit():
#                 data_types[column] = 'float'
#             else:
#                 data_types[column] = 'string'
#         elif data_types[column] == 'integer':
#             # If the data type is integer, check that the value is a valid integer
#             try:
#               if not value.isdigit():
#                    raise (f'{column} must be an integer')
                  
#             except:
#                 pass
               
#         elif data_types[column] == 'float':
#             # If the data type is float, check that the value is a valid float
#             try:
#               if not value.replace('.', '', 1).isdigit():
#                   pass
#             except:
#                 raise (f'{column} must be a float')

#         # Add the value to the row data dictionary
#         row_data[column] = value

#     # Check for duplicate rows
#     try:
#      if row_data in rows_data:
#         duplicate_row.append(row_data)
#     except:
#             raise (f'Duplicate row found')

#     rows_data.append(row_data)

# # Check for duplicate values
# for column in columns:
#     if len(column_data[column]) != len(set(column_data[column])):
#         pass
#         #raise serializers.ValidationError(f'{column} contains duplicate values')

# # Return a dictionary with the column names, data types, and data size
# print(
#     f'columns: {columns} data_types: {data_types}, duplicate_row:{duplicate_row},empty_count:{empty_count} null_count:{null_count}, rows_data: {rows_data},column_data: {column_data}')

