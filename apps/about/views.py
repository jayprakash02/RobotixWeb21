from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.


class TeamApi(APIView):

    def get(self,request,*args, **kwargs):
        Convenor = Team.objects.filter(post_assign="CC").all()
        Manager = Team.objects.filter(post_assign="MM").all()
        Coordinator = Team.objects.filter(post_assign="CO").all()

        serializer1 = TeamSerializer(Convenor, many=True)
        serializer2 = TeamSerializer(Manager,many=True)
        serializer3 = TeamSerializer(Coordinator,many=True)

        dict = {'Convenor' : serializer1.data ,'Manager' : serializer2.data, 'Coordinator' : serializer3.data}

        return Response(dict)


class Alumini(APIView):

    def get(self,request,*args, **kwargs):
        Alumini = Team.objects.filter(post_assign="AA").all()
        serializer1 = TeamSerializer(Alumini , many=True)
        return Response(serializer1.data)