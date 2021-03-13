""" RobotixWeb URL Configuration """

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
    path('api/achievements/', include('achievements.urls'), name="achievements"),
    path('api/certificate/', include('certificate.urls'), name="certificate"),
    path('api/contact/', include('contact.urls'), name="contact"),
    path('api/events/', include('events.urls'), name="events"),
    path('api/extras/', include('extras.urls'), name="extras"),
    path('api/gallery/', include('gallery.urls'), name="gallery"),
    path('api/roboexpo/', include('roboexpo.urls'), name="roboexpo"),
    path('api/roboPortal/', include('roboPortal.urls'), name="roboPortal"),
    path('api/users/', include('users.urls'), name="users"),
    path('api/workshops/', include('roboPortal.urls'), name="roboPortal"),



    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
    path('', TemplateView.as_view(template_name='index.html')),
]
