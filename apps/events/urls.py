from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'events'

urlpatterns = [
    path('',views.event_api,name='event_api'),
]
