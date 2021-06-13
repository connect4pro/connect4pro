# from django.shortcuts import render, get_object_or_404
# from rest_framework.decorators import api_view
# from django.http import JsonResponse
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework.relations import StringRelatedField
# from .models import Question, Answer, Result
# from django.db.models import Avg
# from rest_framework import serializers, status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, CreateAPIView
# from polls.serializers import QuestionSerializer, AnswerSerializer, ResultSerializer

# class QuestionList(APIView):
#     def get(self, request):
#         questions = Question.objects.all()
#         serializer = QuestionSerializer(questions, many = True)
#         return Response(serializer.data)


# class AnswerList(APIView):
#     def get(self, request):
#         answers = Answer.objects.all()
#         serializer = AnswerSerializer(answers, many = True)
#         return Response(serializer.data)


# class ResultList(APIView):
#     def get(self, request):
#         result = Result.objects.all()
#         serializer = ResultSerializer(result, many = True)
#         print(Result.objects.aggregate(Avg('user_answer')))
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ResultSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ResultCreate(CreateAPIView):
#     serializer_class = ResultSerializer

from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Answer, Question


class GetQuestion(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get(self, request, format=None):
        questions = Question.objects.filter(visible=True, )
        last_point = QuestionSerializer(questions, many=True)
        return Response(last_point.data)


class QuestionAnswer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def post(self, request, format=None):
        answer = AnswerSerializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            return Response({'result': 'OK'})