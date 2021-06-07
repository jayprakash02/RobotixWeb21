from django.urls import path, include
from rest_framework import routers
# from .views import FormResponsesViewset, QuestionsForRecruitmentViewset, FormResponsesAPIView
from .views import FormResponsesAPIView


# router = routers.DefaultRouter()
# router.register(r'form_responses', FormResponsesViewset)
# router.register(r'questionset_recruit', QuestionsForRecruitmentViewset)

app_name = 'recruitment'

urlpatterns = [
    # path('', include(router.urls)), 
    path('', FormResponsesAPIView.as_view())
]   