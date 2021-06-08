from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


from .serializers import QuestionsSerializer, FormResponsesSerializer, SubmittedUserSerializer
from .models import Questions, FormResponses, SubmittedUser
# Create your views here.


class QuestionsView(APIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    def get(self, request, *args, **kwargs):
        if self.request.data.__contains__("Domain"):
            question_dic = {}
            for i in self.request.data["Domain"]:
                question_instance = self.queryset.filter(
                    question_for_domain=i)
                serializer_ = self.serializer_class(question_instance, many=True)
                question_dic[i]=serializer_.data
            return Response(question_dic, status=status.HTTP_200_OK)
        else:
            return Response("Choose Your Domain",status=status.HTTP_400_BAD_REQUEST)



class CandidateFormResponsesAPIView(APIView):
    queryset1 = SubmittedUser.objects.all()
    queryset2 = FormResponses.objects.all()

    def get(self, request, *args, **kwargs):

        serializer_class1 = SubmittedUserSerializer(self.queryset1, many=True)
        serializer_class2 = FormResponsesSerializer(self.queryset2, many=True)

        candidate_dict = {'CandidateData': serializer_class1.data,
                          'CandidateResponses': serializer_class2.data}

        return Response(candidate_dict)
