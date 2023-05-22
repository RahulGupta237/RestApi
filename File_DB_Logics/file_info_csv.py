
from io import TextIOWrapper
import csv


def validate_file(file):
        # Check if the uploaded file is a CSV file
        value=file
        if not value.endswith('.csv'):
            raise ('File must be a CSV file')

        # Parse the CSV file and extract the required information
        #file = TextIOWrapper(file, encoding='utf-8')
        reader = csv.reader(value)
        headers = next(reader)
        columns = []
        for header in headers:
            # Check if the column contains any null values
            has_null = False
            for row in reader:
                if not row[headers.index(header)]:
                    has_null = True
                    break
            if has_null:
                null_check = 'Fail'
            else:
                null_check = 'Pass'
                
            # Check the data type and size of the column
            types = []
            sizes = []
            for row in csv.DictReader(file):
                value = row[header].strip()
                if value:
                    if value.isdigit():
                        types.append('int')
                        sizes.append(len(value))
                    elif value.replace('.','',1).isdigit():
                        types.append('float')
                        sizes.append(len(value))
                    else:
                        types.append('string')
                        sizes.append(len(value))
                else:
                    types.append('null')
                    sizes.append(0)
            data_type = set(types)
            size_of_data = sum(sizes)
            
            # Add the column information to the list
            columns.append({
                'column': header,
                'data_type': data_type,
                'size_of_data': size_of_data,
                'null_check': null_check
            })
           

        return columns

obj=validate_file("test.csv")
print(obj)