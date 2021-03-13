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
        model = sponsors
        fields = '__all__'


class SponserViewSet(viewsets.ModelViewSet):
    queryset = sponsors.objects.all()
    serializer_class = SponsorSerializer

