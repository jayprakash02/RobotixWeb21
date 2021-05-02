""" RobotixWeb URL Configuration """

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

schema_view = get_swagger_view(title='Robotix Club Web2 API')

urlpatterns = [
    re_path(r'^$',schema_view,name="documentationn"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),

    #apps urls
    path('about/', include('about.urls'), name="about"),
    path('achievements/', include('achievements.urls'), name="achievements"),
    path('certificate/', include('certificate.urls'), name="certificate"),
    path('contact/', include('contact.urls'), name="contact"),
    path('events/', include('events.urls'), name="events"),
    path('extras/', include('extras.urls'), name="extras"),
    path('gallery/', include('gallery.urls'), name="gallery"),
    path('roboexpo/', include('roboexpo.urls'), name="roboexpo"),
    path('roboPortal/', include('roboPortal.urls'), name="roboPortal"),
    path('users/', include('users.urls'), name="users"),
    path('workshops/', include('roboPortal.urls'), name="roboPortal"),

]
