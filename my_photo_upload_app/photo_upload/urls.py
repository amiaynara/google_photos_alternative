from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhotoUploadViewSet

router = DefaultRouter()
router.register(r'photos', PhotoUploadViewSet, basename='photo')

urlpatterns = [
    path('', include(router.urls)),
]
