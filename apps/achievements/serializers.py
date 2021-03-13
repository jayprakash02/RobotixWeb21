from rest_framework import serializers,viewsets
from .models import Achievements

class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievements
        fields = '__all__'

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievements.objects.all()
    serializer_class = AchievementSerializer