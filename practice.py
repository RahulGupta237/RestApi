import pandas as pd

# read csv file into a pandas dataframe
df = pd.read_csv('kell-etl/media/files/olympics_BnXyNQh.csv')

# extract a column from the dataframe
my_column = df.columns

# count the number of duplicate rows in the column
num_duplicates = df.duplicated().sum()

# count the number of null values in the column
num_nulls = df.columns.isnull().sum()

# determine the data type of the column
data_type = df.columns.dtype

# print the results
# print(f"Column: {my_column}")
# print(f"Number of duplicates: {num_duplicates}")
# print(f"Number of nulls: {num_nulls}")
# print(f"Data type: {data_type}")

describe=df.describe(include='all')
row_iter = describe.iterrows
print(f"iterrow",row_iter)
info=df.info(show_counts=True)
data_type=df.dtypes
print(describe.to_dict())

# print(info)
print(data_type.to_dict())
input_dict={"data":describe.to_dict()}
print("testing start")
print(input_dict)
print("testing  end")
output_list = []
for column_name, column_data in input_dict["data"].items():
    print("**************************")
    print(column_name)
    print(df[column_name].dtypes)
    print(f"data of each column",input_dict["data"][column_name]["count"])
    print(f"data of each column",input_dict["data"][column_name]["unique"])
    print(f"data of each column",input_dict["data"][column_name]["mean"])
    print(f"data of each column",input_dict["data"][column_name]["max"])
    print(f"data of each column",input_dict["data"][column_name]["25%"])
    print(f"data of each column",input_dict["data"][column_name]["top"])
    print(f"data of each column",type(input_dict["data"][column_name]["count"]))
    print(f"data of each column",type(input_dict["data"][column_name]["unique"]))
    print(f"data of each column",type(input_dict["data"][column_name]["mean"]))
    print(f"data of each column",type(input_dict["data"][column_name]["max"]))
    print(f"data of each column",type(input_dict["data"][column_name]["25%"]))
    print(f"data of each column",type(input_dict["data"][column_name]["top"]))


    print()

  
    
    column_data["column_name"]=column_name

    output_list.append(column_data)
   
import json
output_dict = {"data": output_list}
json_data = json.dumps(output_dict)

print(output_dict)
print("***********************")
print(json_data)

print("****************************")

