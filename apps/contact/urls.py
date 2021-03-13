from django.urls import path,include
from .serializers import ContactViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', ContactViewset)

urlpatterns = [
    path('',include(router.urls),name='contact_api')
]
