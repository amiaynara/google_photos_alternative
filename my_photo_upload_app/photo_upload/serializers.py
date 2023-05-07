from django.core.files.storage import default_storage
from rest_framework import serializers
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image', 'storage_class')

    def save(self, storage_class=None, *args, **kwargs):
        if storage_class:
            default_storage.default_acl = 'private'
            default_storage.object_parameters = {'StorageClass': storage_class}
        return super().save(*args, **kwargs)