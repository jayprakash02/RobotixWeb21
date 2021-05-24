from rest_framework import serializers, viewsets
from .models import *


class DIYSerializer(serializers.ModelSerializer):
    class Meta:
        model = DIY
        fields = "__all__"


class DIYViewSet(viewsets.ModelViewSet):
    queryset = DIY.objects.all()
    serializer_class = DIYSerializer


class FYISerializer(serializers.ModelSerializer):
    class Meta:
        model = FYI
        fields = "__all__"


class FYIViewSet(viewsets.ModelViewSet):
    queryset = FYI.objects.all()
    serializer_class = FYISerializer


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = '__all__'


class SponserViewSet(viewsets.ModelViewSet):
    queryset = Sponsors.objects.all()
    serializer_class = SponsorSerializer


class WebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web
        fields = "__all__"


class WebViewSet(viewsets.ModelViewSet):
    queryset = DIY.objects.all()
    serializer_class = DIYSerializer


class GallerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gallery
        fields = "__all__"

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class ContactViewset(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer