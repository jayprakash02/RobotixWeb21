from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import QuestionsSerializer, FormResponsesSerializer, SubmittedUserSerializer
from .models import Questions, FormResponses, SubmittedUser
# Create your views here.


class QuestionsView(APIView):
    queryset_openall = Questions.objects.filter(question_for_domain="All")
    queryset_web = Questions.objects.filter(question_for_domain="Web")
    queryset_design = Questions.objects.filter(question_for_domain="Design")
    queryset_pr = Questions.objects.filter(question_for_domain="PR")
    queryset_core = Questions.objects.filter(question_for_domain="Core")
    queryset_docs = Questions.objects.filter(question_for_domain="Docs")

    def get(self, request, *args, **kwargs):

        serializer_class_openall = QuestionsSerializer(self.queryset_openall, many=True)
        serializer_class_web = QuestionsSerializer(self.queryset_web, many=True)
        serializer_class_design = QuestionsSerializer(self.queryset_design, many=True)
        serializer_class_pr = QuestionsSerializer(self.queryset_pr, many=True)
        serializer_class_core = QuestionsSerializer(self.queryset_core, many=True)
        serializer_class_docs = QuestionsSerializer(self.queryset_docs, many=True)

        hashy = {
            'openall': serializer_class_openall.data,
            'web': serializer_class_web.data,
            'design': serializer_class_design.data,
            'pr': serializer_class_pr.data,
            'core': serializer_class_core.data,
            'docs':serializer_class_docs.data
        }
        return Response(hashy)



class CandidateFormResponsesAPIView(APIView):
    queryset1 = SubmittedUser.objects.all()
    queryset2 = FormResponses.objects.all()
    
    def get(self,request,*args, **kwargs):

        serializer_class1 = SubmittedUserSerializer(self.queryset1, many=True)
        serializer_class2 = FormResponsesSerializer(self.queryset2, many=True)

        candidate_dict = {'CandidateData' : serializer_class1.data ,'CandidateResponses' : serializer_class2.data}

        return Response(candidate_dict)
