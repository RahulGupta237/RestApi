import csv
reader = csv.DictReader("My_People.csv")

        # Create a list of column names
columns = reader.fieldnames

# Create a dictionary to store the data type for each column
data_types = {}
for column in columns:
    data_types[column] = None

# Create a list to store the data of each row
rows_data = []

# Create a dictionary to store the data of each column
column_data = {}
for column in columns:
    column_data[column] = []
    # Create a set to store the row data
row_set = set()

# Create a variable to store the number of null values
null_count = 0
empty_count=0
duplicate_row=[]
# Iterate over the rows in the CSV file to infer data types and check for null values, empty values, and duplicate values
for row in reader:
    row_data = {}
    for column in columns:
        value = row[column]

        # Check for null values
        if value is None:
            null_count += 1
            continue
            

        # Check for empty values
        if value.strip() == '':
            empty_count += 1
            continue

        # Add the value to the column data list
        column_data[column].append(value)

        # Infer data types
        if not value:
            continue
        elif data_types[column] is None:
            # If the data type has not been inferred yet, try to infer it from the first row
            if value.isdigit():
                data_types[column] = 'integer'
            elif value.replace('.', '', 1).isdigit():
                data_types[column] = 'float'
            else:
                data_types[column] = 'string'
        elif data_types[column] == 'integer':
            # If the data type is integer, check that the value is a valid integer
            try:
              if not value.isdigit():
                   raise (f'{column} must be an integer')
                  
            except:
                pass
               
        elif data_types[column] == 'float':
            # If the data type is float, check that the value is a valid float
            try:
              if not value.replace('.', '', 1).isdigit():
                  pass
            except:
                raise (f'{column} must be a float')

        # Add the value to the row data dictionary
        row_data[column] = value

    # Check for duplicate rows
    try:
     if row_data in rows_data:
        duplicate_row.append(row_data)
    except:
            raise (f'Duplicate row found')

    rows_data.append(row_data)

# Check for duplicate values
for column in columns:
    if len(column_data[column]) != len(set(column_data[column])):
        pass
        #raise serializers.ValidationError(f'{column} contains duplicate values')

# Return a dictionary with the column names, data types, and data size
print(
    f'columns: {columns} data_types: {data_types}, duplicate_row:{duplicate_row},empty_count:{empty_count} null_count:{null_count}, rows_data: {rows_data},column_data: {column_data}')


