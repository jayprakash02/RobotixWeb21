from django.urls import path, include
from rest_framework import routers
from .serializers import *

router = routers.DefaultRouter()
router.register(r'sponsors', SponserViewSet)
router.register(r'diy', DIYViewSet)
router.register(r'fyi', FYIViewSet)

app_name = 'info'

urlpatterns = [
    path('',include(router.urls)),
]
