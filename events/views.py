from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event, EventComment
from events.serializers import EventSerializer, EventCommentSerializer


class EventList(APIView):
    """Список мероприятий"""
    permission_classes = ()

    @swagger_auto_schema(responses={200: EventSerializer(many=True)})
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventDetail(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'

class EventCommentsList(ListAPIView):
    queryset = EventComment.objects.all()
    serializer_class = EventCommentSerializer


# class EventCommentsList(APIView):
#     """Список комментариев мероприятий"""
#     permission_classes = ()
#
#     @swagger_auto_schema(responses={200: EventCommentSerializer(many=True)})
#     def get(self, request):
#         event_comments = EventComment.objects.all()
#         serializer = EventCommentSerializer(event_comments, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         """Создание мероприятия"""
#         serializer = EventCommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventCommentCreate(CreateAPIView):
    serializer_class = EventCommentSerializer
