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

class QuestionCreate(CreateAPIView):
    serializer_class = QuestionSerializer



class ChoiceList(APIView):
     def get(self, request):
         choices = Choice.objects.all()
         serializer = ChoiceSerializer(choices, many = True)
         return Response(serializer.data)

class ChoiceCreate(CreateAPIView):
    serializer_class = ChoiceSerializer


class AnswerList(APIView):
     def get(self, request):
         answer = Answer.objects.all()
         serializer = AnswerSerializer(answer, many = True)
         return Response(serializer.data)

class AnswerCreate(CreateAPIView):
    serializer_class = AnswerSerializer



class PollResultList(APIView):
    def get(self, request):
        poll_results = ResultPoll.objects.all()
        serializer = ResultPollSerializer(poll_results, many = True)
        # total_points = ResultPoll.objects.aggregate(Sum('answers'))['answers__sum']
        # num_matches = Answer.objects.count()
        # average_points_per_match = total_points / num_matches
        # print(average_points_per_match)
        count_answers = ResultPoll.objects.get(id = 1)
        print(count_answers)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResultPollSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class PollResultCreate(CreateAPIView):
    serializer_class = ResultPollSerializer