"""
RobotixWeb URL Configuration
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),

    #apps urls
    path('api/about/', include('about.urls'), name="about"),
    path('api/achievements/', include('achievements.urls'), name="about"),
    path('api/certificate/', include('certificate.urls'), name="about"),
    path('api/contact/', include('contact.urls'), name="about"),
    path('api/events/', include('events.urls'), name="about"),
    path('api/extras/', include('extras.urls'), name="about"),

    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
    path('', TemplateView.as_view(template_name='index.html')),

    
]
