from django.db import models
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    storage_class = models.CharField(max_length=32, choices=[
        ('STANDARD', 'STANDARD'), ('DEEP_ARCHIVE', 'DEEP_ARCHIVE')
    ])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the original image first
        # Create a thumbnail
        img = Image.open(self.image.path)
        img.thumbnail((200, 200))  # Set the desired thumbnail size, e.g., 200x200 pixels

        # Save the thumbnail
        buffer = BytesIO()
        img.save(buffer, format='JPEG')
        file_name = f'thumbnail_{self.image.name}'
        file_buffer = InMemoryUploadedFile(buffer, None, file_name, 'image/jpeg', sys.getsizeof(buffer), None)
        thumbnail = Thumbnail(photo=self, image=file_buffer)
        thumbnail.save()

class Thumbnail(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnails/')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)