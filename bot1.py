import boto3
import botocore.exceptions
# Create an S3 client
listi=[]
try:
    s3 = boto3.client('s3', aws_access_key_id='AKIAQJBGBNSCQEP3RUXN', 
    aws_secret_access_key='Hg6OXwHVNjDmtvHTNnGT6P',
    region_name='ap-south-1')

    bucket_name = 'kell-etl-vm'
    response = s3.list_objects(Bucket=bucket_name)



    # Extract the file keys from the response  kapiljuneja@kellton.com Kapil@237
    file_keys = [obj['Key'] for obj in response['Contents']]

    print(file_keys)
    for i in file_keys:
        local_file_path = f'/home/rl/Documents/practice_poc/kell-etl/media/S2bucket/{i}'
        file_name = f"{i}"
        s3.download_file(bucket_name, file_name, local_file_path)
        print("file sucessfully updated")
except:
    
        print("rahul you fault")

if listi:
    print(listi)
else:
    print("i love you ")

