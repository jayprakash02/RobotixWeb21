from django.urls import path,include
from .serializers import *

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'sponsors', SponserViewSet)
router.register(r'diy', DIYViewSet)
router.register(r'fyi', FYIViewSet)

app_name = 'info'
urlpatterns = [
    path('',include(router.urls)),
]
