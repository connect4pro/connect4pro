from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.relations import StringRelatedField
from .models import Author, Category, Post, Reply, Comment
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, CreateAPIView
from forum.serializers import AuthorSerializer, CategorySerializer, PostSerializer, ReplySerializer, CommentSerializer
from .utils import update_views



#AuthorList
class AuthorList(APIView):
    permission_classes = ()

    @swagger_auto_schema(responses = {200: AuthorSerializer(many = True)})
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many = True)
        return Response(serializer.data)

    def post(self, request):
        """Создание мероприятия"""
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#AuthorCreate
class AuthorCreate(CreateAPIView):
    serializer_class = AuthorSerializer


#CategoryList
class CategoryList(APIView):
    permission_classes = ()

    @swagger_auto_schema(responses = {200: CategorySerializer(many = True)})
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data)

    def post(self, request):
        """Создание категории"""
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#CategoryCreate
class CategoryCreate(CreateAPIView):
    serializer_class = CategorySerializer



#PostList
class PostList(APIView):
    permission_classes = ()

    @swagger_auto_schema(responses = {200: PostSerializer(many = True)})
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#PostCreate
class PostCreate(CreateAPIView):
    serializer_class = PostSerializer


#ReplyList
class ReplyList(APIView):
    permission_classes = ()

    @swagger_auto_schema(responses = {200: ReplySerializer(many = True)})
    def get(self, request):
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#ReplyCreate
class ReplyCreate(CreateAPIView):
    serializer_class = ReplySerializer



#CommentList
class CommentList(APIView):
    permission_classes = ()

    @swagger_auto_schema(responses = {200: CommentSerializer(many = True)})
    def get(self, request):
        comments = Comment.objects.all()
        serializer = ReplySerializer(comments, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#CommentCreate
class CommentCreate(CreateAPIView):
    serializer_class = CommentSerializer