from rest_framework import serializers
from .models import QuestionsForRecruitment, FormResponses
from rest_framework import viewsets, permissions



class QuestionsForRecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsForRecruitment
        fields = "__all__"


class QuestionsForRecruitmentViewset(viewsets.ModelViewSet):
    queryset = QuestionsForRecruitment.objects.all()
    permission_classes = [  
        permissions.AllowAny
    ]
    serializer_class = QuestionsForRecruitmentSerializer





## Form responses Serializers and viewsets
class FormResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormResponses
        fields = "__all__"


class FormResponsesViewset(viewsets.ModelViewSet):
    queryset = FormResponses.objects.all()
    permission_classes = [  
        permissions.AllowAny
    ]
    serializer_class = FormResponsesSerializer