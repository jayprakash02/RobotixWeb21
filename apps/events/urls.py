
from django.urls import path
from . import views
urlpatterns = [
    # path('',views.event,name='event'),
    path('',views.event_api,name='event_api')
]
