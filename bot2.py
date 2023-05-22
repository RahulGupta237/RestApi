
# Get the S3 client object
import boto3
session = boto3.Session(
    aws_access_key_id='AKIAQJBGBNSCQEP3RUXN', 
    aws_secret_access_key='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',
    region_name='ap-south-1'
    )
s3 = session.client('s3')

# Download the file from the S3 bucket to a local directory
s3.download_file('your_bucket_name', 'mypeople.csv', '/kell-etl/rahul.csv')