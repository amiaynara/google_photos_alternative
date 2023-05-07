from rest_framework import viewsets
from .models import Photo
from .serializers import PhotoSerializer

class PhotoUploadViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        storage_class = self.request.data.get('storage_class')
        serializer.save(storage_class=storage_class)
