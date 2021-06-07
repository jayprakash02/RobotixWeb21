from rest_framework import serializers
from .models import QuestionsForRecruitment, FormResponses



class QuestionsForRecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsForRecruitment
        fields = "__all__"


## Form responses Serializers and viewsets
class FormResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormResponses
        fields = "__all__"


