from rest_framework import serializers, viewsets
from .models import *


class RoboexpoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roboexpo
        fields = "__all__"


class RoboexpoViewSet(viewsets.ModelViewSet):
    queryset = Roboexpo.objects.all()
    serializer_class = RoboexpoSerializer
