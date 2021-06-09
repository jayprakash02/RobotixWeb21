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
        question_ = {}
        question_tance = self.queryset.filter(question__domain="All")
        serializer_ = self.serializer_class(question_tance, many=True)
        question_["All"] = serializer_.data
        if self.request.data.__contains__("Domain"):
            for i in self.request.data["Domain"]:
                question_tance = self.queryset.filter(
                    question__domain=i)
                serializer_ = self.serializer_class(question_tance, many=True)
                question_[i]=serializer_.data
            return Response(question_, status=status.HTTP_200_OK)
        else:
            return Response(question_,status=status.HTTP_400_BAD_REQUEST)



class CandidateFormResponsesAPIView(APIView):
    queryset1 = SubmittedUser.objects.all()
    queryset2 = FormResponses.objects.all()

    def get(self, request, *args, **kwargs):

        serializer_class1 = SubmittedUserSerializer(self.queryset1, many=True)
        serializer_class2 = FormResponsesSerializer(self.queryset2, many=True)

        candidate_dict = {'CandidateData': serializer_class1.data,
                          'CandidateResponses': serializer_class2.data}

        return Response(candidate_dict)

    def post(self,request):
        if self.request.data.__contains__("Name") and self.request.data.__contains__("ID") and self.request.data.__contains__("Mobile") and self.request.data.__contains__("Email") and self.request.data.__contains__("Domain") and self.request.data.__contains__("Question"):
            name = self.request.data["Name"]
            response_id = self.request.data["ID"]
            mobile = self.request.data["Mobile"]
            email = self.request.data["Email"]
            domain = self.request.data["Domain"]
            question = self.request.data["Question"]

            candidate = SubmittedUser.objects.create(candidate_name=name,candidate_id=response_id,candidate_mobile_number=mobile,candidate_emailid=email,candidate_domain_choices=domain)
            candidate.save()
            if question["All"]:
                question_ = question["All"]
                for q in question_:
                    question_instance = Questions.objects.filter(q["ID"])
                    if question_instance.exists:
                        candiateResponse = FormResponses.objects.create(question_id=q["ID"],submitted_candidate_id=response_id,answer_given=q["Answer"])
                        candiateResponse.save()
            if question["Web"]:
                question_ = question["Web"]
                for q in question_:
                    question_instance = Questions.objects.filter(q["ID"])
                    if question_instance.exists:
                        candiateResponse = FormResponses.objects.create(question_id=q["ID"],submitted_candidate_id=response_id,answer_given=q["Answer"])
                        candiateResponse.save()
            if question["PR"]:
                question_ = question["PR"]
                for q in question_:
                    question_instance = Questions.objects.filter(q["ID"])
                    if question_instance.exists:
                        candiateResponse = FormResponses.objects.create(question_id=q["ID"],submitted_candidate_id=response_id,answer_given=q["Answer"])
                        candiateResponse.save()
            if question["Design"]:
                question_ = question["Design"]
                for q in question_:
                    question_instance = Questions.objects.filter(q["ID"])
                    if question_instance.exists:
                        candiateResponse = FormResponses.objects.create(question_id=q["ID"],submitted_candidate_id=response_id,answer_given=q["Answer"])
                        candiateResponse.save()
            if question["Core"]:
                question_ = question["Core"]
                for q in question_:
                    question_instance = Questions.objects.filter(q["ID"])
                    if question_instance.exists:
                        candiateResponse = FormResponses.objects.create(question_id=q["ID"],submitted_candidate_id=response_id,answer_given=q["Answer"])
                        candiateResponse.save()
            if question["Docs"]:
                question_ = question["Docs"]
                for q in question_:
                    question_instance = Questions.objects.filter(q["ID"])
                    if question_instance.exists:
                        candiateResponse = FormResponses.objects.create(question_id=q["ID"],submitted_candidate_id=response_id,answer_given=q["Answer"])
                        candiateResponse.save()

            return Response(self.request.data["Question"]["All"][0]["ID"])
        return Response(self.request.data["Questions"],status=status.HTTP_400_BAD_REQUEST)
