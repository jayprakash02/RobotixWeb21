from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

import secrets
import string
import hashlib


# Create your views here.


class TeamApi(APIView):

    def get(self, request, *args, **kwargs):
        Convenor = Team.objects.filter(post_assign="CC").all()
        Manager = Team.objects.filter(post_assign="MM").all()
        Coordinator = Team.objects.filter(post_assign="CO").all()

        serializer1 = TeamSerializer(Convenor, many=True)
        serializer2 = TeamSerializer(Manager, many=True)
        serializer3 = TeamSerializer(Coordinator, many=True)

        dict = {'Convenor': serializer1.data,
                'Manager': serializer2.data, 'Coordinator': serializer3.data}

        return Response(dict)


class Alumini(APIView):

    def get(self, request, *args, **kwargs):
        Alumini = Team.objects.filter(post_assign="AA").all()
        serializer1 = TeamSerializer(Alumini, many=True)
        return Response(serializer1.data)


class VerifyEmail(APIView):

    def post(self, request, *args, **kwargs):
        email_add = request.POST.get('email')
        otp = ''.join(secrets.choice(string.ascii_uppercase +
                      string.digits) for i in range(6))
        send_mail('OTP for information update', 'Your OTP for information update is ' + otp +
                  '\nThis OTP is valid for the next 5 minutes', settings.EMAIL_HOST_USER, [email_add], fail_silently=False)
        hs = hashlib.sha256(otp.encode('utf-8'))
        return Response(hs.hexdigest())
