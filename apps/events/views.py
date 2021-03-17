from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer


# Create your views here.

@api_view()
def event_api(request):
    obj_event = Event.objects.all()
    serializer1 = EventSerializer(obj_event,many=True)
    dict = {'Event':serializer1.data}

    return Response(dict)
