from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.relations import StringRelatedField
from .models import Question, Choices, GetPoll
from django.db.models import Avg
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, CreateAPIView
from polls.serializers import QuestionSerializer, ChoicesSerializer, GetPollSerializer

class QuestionList(APIView):
    def get(self, request):
        questions_list = Question.objects.all()
        serializer = QuestionSerializer(questions_list, many = True)
        return Response(serializer.data)

class ChoicesList(APIView):
    def get(self, request):
        choices_list = Choices.objects.all()
        serializer = ChoicesSerializer(choices_list, many = True)
        return Response(serializer.data)

class GetPollList(APIView):
    def get(self, request):
        poll = GetPoll.objects.all()
        serializer = GetPollSerializer(poll, many = True)
        return Response(serializer.data)