from django.urls import path,include
from rest_framework import routers
from .serializers import AchievementViewSet

router = routers.DefaultRouter()
router.register(r'', AchievementViewSet)

urlpatterns = [
    path('',include(router.urls),name='achievement_api')
]
