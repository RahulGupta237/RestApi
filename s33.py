import boto3
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def upload_csv(request):
    # Get file name and S3 bucket name from request data
    file_name = request.data.get('file_name')
    bucket_name = request.data.get('bucket_name')

    # Set up S3 client
    s3 = boto3.client('s3')

    # Download CSV file from S3 to a temporary file
    with open('temp.csv', 'wb') as f:
        s3.download_fileobj(bucket_name, file_name, f)

    # Set up file path and name for the media folder
    file_path = 'path/to/your/media/folder/' + file_name

    # Open CSV file and read content
    with open('temp.csv', 'r') as f:
        csv_content = f.read()

    # Save CSV content to Django's default storage in the media folder
    file = ContentFile(csv_content)
    file_name = default_storage.save(file_path, file)

    # Clean up temporary file
    import os
    os.remove('temp.csv')

    # Return success response
    return Response({'success': True, 'file_name': file_name})
