from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from . import views
from .serializers import PortalUserViewSet, TeamViewSet, RobothonViewSet 



router = routers.DefaultRouter()
router.register(r'portaluser', PortalUserViewSet)
router.register(r'team', TeamViewSet)
router.register(r'robothon', RobothonViewSet)


urlpatterns = [
    path('',include(router.urls)),
]


# urlpatterns = [
#     path('registration/',views.home,name= "home"),
#     path('registration/api/',views.home_api,name= "home_api"),
#     path('problem-statements/',views.problem_statements,name='problem-statement'),
#     path('problem-statements/api/',views.problem_statements_api,name='problem-statement-api'),
#     path('createProfile/', views.createProfile, name="createProfile"),
#     path('adminView/',views.adminView, name= "adminView"),
#     path('profileView/<int:user_id>/',views.profileView, name= "profileView"),
#     path('select/<int:team_id>',views.select, name="select"),
#     path('confirm/<str:token>/',views.confirm, name="confirm"),
# ]
