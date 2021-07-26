from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status, generics
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from faq.models import WriteUs, QuestionsAndAnswers
from faq.serializers import WriteUsSerializer, QuestionsAndAnswersSerializer


class QuestionsAndAnswersList(APIView):
    """Список всех вопросов и ответов"""
    permission_classes = ()

    @swagger_auto_schema(responses={200: QuestionsAndAnswersSerializer(many=True)})
    def get(self, request):
        questions_and_answers = QuestionsAndAnswers.objects.all()
        serializer = QuestionsAndAnswersSerializer(questions_and_answers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: QuestionsAndAnswersSerializer()})
    def post(self, request):
        """Создание вопроса и ответа"""
        serializer = QuestionsAndAnswersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionsAndAnswersCreate(CreateAPIView):
    """Создание вопроса и ответа"""
    serializer_class = QuestionsAndAnswersSerializer


class WriteUsList(APIView):
    """Список сообщений, присланные пользователями через форму <<Напишите нам>>"""
    permission_classes = ()

    @swagger_auto_schema(responses={200: WriteUsSerializer(many=True)})
    def get(self, request):
        write_us = WriteUs.objects.all()
        serializer = WriteUsSerializer(write_us, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: WriteUsSerializer()})
    def post(self, request):
        """Создание сообщения через форму <<Напишите нам>>"""
        serializer = WriteUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class WriteUsCreate(CreateAPIView):
    """Создание сообщения через форму <<Напишите нам>>"""
    serializer_class = WriteUsSerializer