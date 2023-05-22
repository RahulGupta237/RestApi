from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from myapp.models import MyModel

# Set up file path and name
file_path = 'path/to/your/media/folder/your_file_name.csv'

# Open CSV file and read content
with open('path/to/your/csv/file.csv', 'r') as f:
    csv_content = f.read()

# Save CSV content to Django's default storage in the media folder
file = ContentFile(csv_content)
file_name = default_storage.save(file_path, file)

# Create a new model instance with the file field set to the uploaded file
my_model = MyModel.objects.create(file_field=file_name)

# Print the URL of the uploaded file
print(my_model.file_field.url)
