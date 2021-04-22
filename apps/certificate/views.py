from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Certificate

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CertificateSerializer


class CertificateView(APIView):
    def get(self,request,*args, **kwargs):
        pass

    def post(self,request,*args, **kwargs):
        url_key = request.POST.get('url_key')
        try:
            obj = get_object_or_404(Certificate,url_key=url_key)
            event = str(obj.event.title)
            name = str(obj.name)
            image = str(obj.image.url)
            dict ={'name':name,'image':image,'event':event}
        except Http404:
            dict ={'error':'NOT FOUND'}
        return Response(dict)