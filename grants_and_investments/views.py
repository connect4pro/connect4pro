from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status, generics
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from grants_and_investments.models import Grant, Investment
from grants_and_investments.serializers import GrantSerializer, InvestmentSerializer
# Create your views here.

class GrantList(APIView):
    """Список всех грантов"""
    permission_classes = ()

    @swagger_auto_schema(responses={200: GrantSerializer(many=True)})
    def get(self, request):
        grants = Grant.objects.all()
        serializer = GrantSerializer(grants, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: GrantSerializer()})
    def post(self, request):
        """Создание гранта"""
        serializer = GrantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GrantCreate(CreateAPIView):
    serializer_class = GrantSerializer


class InvestmentList(APIView):
    """Список инвестиций"""
    permission_classes = ()

    @swagger_auto_schema(responses={200: InvestmentSerializer(many=True)})
    def get(self, request):
        investments = Investment.objects.all()
        serializer = InvestmentSerializer(investments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: InvestmentSerializer()})
    def post(self, request):
        """Создание инвестиции"""
        serializer = InvestmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



class InvestmentCreate(CreateAPIView):
    serializer_class = InvestmentSerializer