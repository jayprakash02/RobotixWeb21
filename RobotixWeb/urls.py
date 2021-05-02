""" RobotixWeb URL Configuration """

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view

from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', schema_view.with_ui('swagger',cache_timeout=0), name='schema-swagger-ui'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),

    #apps urls
    path('users/', include('users.urls'), name="users"),
    path('about/', include('about.urls'), name="about"),
    path('achievements/', include('achievements.urls'), name="achievements"),
    path('certificate/', include('certificate.urls'), name="certificate"),
    path('contact/', include('contact.urls'), name="contact"),
    path('events/', include('events.urls'), name="events"),
    path('extras/', include('extras.urls'), name="extras"),
    path('gallery/', include('gallery.urls'), name="gallery"),
    # path('roboexpo/', include('roboexpo.urls'), name="roboexpo"),
    # path('roboPortal/', include('roboPortal.urls'), name="roboPortal"),
   #  path('workshops/', include('roboPortal.urls'), name="roboPortal"),

]
