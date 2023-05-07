from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from .models import Thumbnail

def upload_to_s3(local_file_path, storage_class, file_name):
    s3_storage = S3Boto3Storage()

    with open(local_file_path, 'rb') as file:
        s3_key = f'photos/{file_name}'
        s3_storage.save(s3_key, file, extra_args={'StorageClass': storage_class})

def generate_thumbnail(image):
    # Create a thumbnail
    img = Image.open(image.path)
    img.thumbnail((200, 200))  # Set the desired thumbnail size, e.g., 200x200 pixels

    # Save the thumbnail
    buffer = BytesIO()
    img.save(buffer, format='JPEG')
    file_name = f'thumbnail_{image.name}'
    file_buffer = InMemoryUploadedFile(buffer, None, file_name, 'image/jpeg', sys.getsizeof(buffer), None)
    
    return Thumbnail(photo=image, image=file_buffer)