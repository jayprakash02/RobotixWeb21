from .serializers import RoboexpoViewSet
from django.urls import path, include
from rest_framework import routers
# from . import views

app_name = 'roboexpo'

router = routers.DefaultRouter()
router.register(r'roboexpo', RoboexpoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    # path('registration/', views.expo, name='roboexpo-registration'),
]
