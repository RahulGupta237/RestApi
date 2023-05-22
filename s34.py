import boto3
import pandas as pd

# Define the S3 bucket and prefix
bucket_name = 'your-bucket-name'
prefix = 'path/to/files/'

# Create an S3 client
s3 = boto3.client('s3')

# List objects in the bucket with the given prefix
objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)['Contents']

# Get a list of the file names
file_names = [obj['Key'] for obj in objects]

# Read each file using pandas
dfs = []
for file_name in file_names:
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    dfs.append(pd.read_csv(obj['Body']))

# Concatenate the dataframes
df = pd.concat(dfs)
