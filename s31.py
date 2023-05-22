import boto3
from django.core.files.storage import default_storage

# Set up S3 client
s3 = boto3.client('s3')

# Set up bucket name and object key
bucket_name = 'your_bucket_name'
object_key = 'your_object_key.csv'

# Download CSV file from S3 to a temporary file
with open('temp.csv', 'wb') as f:
    s3.download_fileobj(bucket_name, object_key, f)

# Upload CSV file to Django's default storage in a specific folder
file_path = 'path/to/your/folder/your_file_name.csv'
default_storage.save(file_path, open('temp.csv', 'rb'))

# Clean up temporary file
import os
os.remove('temp.csv')
