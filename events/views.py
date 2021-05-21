from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event
from events.serializers import EventSerializer

# Create your views here.
"""Список мероприятий"""
class EventList(APIView):
    permission_classes = ()

    @swagger_auto_schema(responses = {200: EventSerializer(many = True)})
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many = True)
        return Response(serializer.data)

    def post(self, request):
        """Создание мероприятия"""
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventCreate(CreateAPIView):
    serializer_class = EventSerializer