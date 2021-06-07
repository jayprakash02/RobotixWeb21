from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import QuestionsForRecruitmentSerializer, FormResponsesSerializer
from .models import QuestionsForRecruitment, FormResponses
# Create your views here.


# class QuestionsForRecruitmentViewset(viewsets.ModelViewSet):
#     queryset = QuestionsForRecruitment.objects.all()
#     permission_classes = [  
#         permissions.AllowAny
#     ]
#     serializer_class = QuestionsForRecruitmentSerializer




# class FormResponsesViewset(viewsets.ModelViewSet):
#     queryset = FormResponses.objects.all()
#     permission_classes = [  
#         permissions.AllowAny
#     ]
#     serializer_class = FormResponsesSerializer




class FormResponsesAPIView(generics.ListAPIView):
    queryset1 = QuestionsForRecruitment.objects.all()
    queryset2 = FormResponses.objects.all()

    serializer_class1 = QuestionsForRecruitmentSerializer
    serializer_class2 = FormResponsesSerializer

    permission_classes = [  
        permissions.AllowAny
    ]

    # dict = {'DIY' : serializer1.data ,'FYI' : serializer2.data  }



# class DIYFYI(APIView):

#     def get(self,request,*args, **kwargs):
#         diy = DIY_FYI.objects.filter(link='').all()
#         fiy = DIY_FYI.objects.filter(file='').all()
#         serializer1 = DIY_FYISerializer(diy , many=True)
#         serializer2 = DIY_FYISerializer(fiy, many=True)
        

#         dict = {'DIY' : serializer1.data ,'FYI' : serializer2.data  }

#         return Response(dict)