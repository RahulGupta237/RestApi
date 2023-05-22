import pandas as pd

# read csv file into a pandas dataframe
df = pd.read_csv('My_People.csv')

# extract a column from the dataframe
my_column = df.columns
print(list(my_column))

for i in list(my_column):
    print(df[i].describe(include="all").to_dict())
# count the number of duplicate rows in the column
# num_duplicates = df.duplicated().sum()

# count the number of null values in the column
num_nulls = df.columns.isnull().sum()

# determine the data type of the column
data_type = df.columns.dtype

# print the results
# print(f"Column: {my_column}")
# print(f"Number of duplicates: {num_duplicates}")
# print(f"Number of nulls: {num_nulls}")
# print(f"Data type: {data_type}")

# describe=df.describe(include='all')
# row_iter = describe.iterrows
# print(f"iterrow",row_iter)
# info=df.info(show_counts=True)
# data_type=df.dtypes
# print(describe.to_dict())

# # print(info)
# print(data_type.to_dict())
# input_dict={"data":describe.to_dict()}
# print("testing start")
# print(input_dict)
# print("testing  end")