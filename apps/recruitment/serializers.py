from rest_framework import serializers
from .models import Questions, FormResponses, SubmittedUser



class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"


## Form responses Serializers and viewsets
class FormResponsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormResponses
        fields = "__all__"


class SubmittedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubmittedUser
        fields = "__all__"