from django.urls import re_path,include, path
from .views import *

app_name = 'certificate'

urlpatterns = [
    path('<uuid:url_key>/', Search, name='search'),
    path('', Search, name='enter_id'),
]