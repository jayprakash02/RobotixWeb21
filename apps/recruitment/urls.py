from django.urls import path, include
from rest_framework import routers
# from .views import FormResponsesViewset, QuestionsViewset, FormResponsesAPIView
from .views import CandidateFormResponsesAPIView, QuestionsView


app_name = 'recruitment'

urlpatterns = [
    path('questions/', QuestionsView.as_view()), 
    path('', CandidateFormResponsesAPIView.as_view())
]   