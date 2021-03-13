from django.urls import path, include
from rest_framework import routers
from .serializers import *


router = routers.DefaultRouter()
router.register(r'gallery', GalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
