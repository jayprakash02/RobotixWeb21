from django.urls import include, path
from .views import *


urlpatterns = [
    path('',CertificateView.as_view()),
]