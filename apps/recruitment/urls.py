from django.urls import path, include
from rest_framework import routers
from .serializers import FormResponsesViewset, QuestionsForRecruitmentViewset


router = routers.DefaultRouter()
router.register(r'form_responses', FormResponsesViewset)
router.register(r'questionset_recruit', QuestionsForRecruitmentViewset)

app_name = 'recruitment'

urlpatterns = [
    path('', include(router.urls)), 
]   