from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import *
from django.db.models import Sum
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, CreateAPIView, GenericAPIView
from polls.serializers import *

class QuestionList(APIView):
     def get(self, request):
         questions = Question.objects.all()
         serializer = QuestionSerializer(questions, many = True)
         return Response(serializer.data)

# class QuestionCreate(CreateAPIView):
#     serializer_class = QuestionSerializer


class AnswerList(APIView):
     def get(self, request):
         answer = Answer.objects.all()
         serializer = AnswerSerializer(answer, many = True)
         return Response(serializer.data)

class AnswerCreate(APIView):
    def post(self, request, question_id, poll_id):

        question = Question.objects.get(id = question_id)
        poll = ResultPoll.objects.get(id = poll_id)
        answer = Answer.objects.create(question = question, poll_result = poll, final_answer = request.data["choice"])
        serializer = AnswerSerializer(answer)
        return Response(serializer.data, status.HTTP_201_CREATED)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status.HTTP_201_CREATED)
        # return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



class PollResultId(APIView):
    def post(self, request):
        serializer = ResultPollSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class PollResultCreate(CreateAPIView):
    serializer_class = ResultPollSerializer