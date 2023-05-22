import boto3
session = boto3.Session(
    aws_access_key_id='AKIAQJBGBNSCQEP3RUXN', 
    aws_secret_access_key='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',
    region_name='ap-south-1'
    )

#Then use the session to get the resource
s3 = session.resource('s3')

my_bucket = s3.Bucket('kell-etl-vm')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)



# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id='AKIAQJBGBNSCQEP3RUXN', 
    aws_secret_access_key='Hg6ObmHgHDWV/Gz4/vHPFLXwHVNjDmtvHTNnGT6P',
    region_name='ap-south-1')

# s3.delete_object(Bucket="kell-etl-vm", Key="dummy_invoice.pdf")
# Specify the bucket name
bucket_name = 'kell-etl-vm'

# Use the S3 client to list all objects in the bucket
response = s3.list_objects(Bucket=bucket_name)
print(response)



# Extract the file keys from the response
file_keys = [obj['Key'] for obj in response['Contents']]
print()
print("************************************")
# Print the list of file keys
print(file_keys)

import pandas as pd
response = s3.get_object(Bucket=bucket_name, Key=file_keys[1])

dataframe=pd.read_csv(response['Body'])
print(dataframe)
# # Determine the encoding of the file
# encoding = response['ContentEncoding'] if 'ContentEncoding' in response else 'utf-8'

# # Decode the file contents using the determined encoding
# file_content = response['Body'].read()

# # # Print the contents of the file
# print(file_content)


# Display the dataframe




# Set up bucket name and object key

# object_key = 'mypeople.csv'

# # Set up file path and name
# file_path = 'My_People.csv'

# # Upload CSV file to S3
# s3.upload_file(file_path, bucket_name, object_key)

url = s3.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': bucket_name ,
        'Key': 'mypeople.csv',
    },
    ExpiresIn=3600  # URL expires after one hour
)
print(f"file path url {url}")