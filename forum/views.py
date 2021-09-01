from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.relations import StringRelatedField
from .models import Author, Category, Post, Comment
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, CreateAPIView
from forum.serializers import AuthorSerializer, CategorySerializer, PostSerializer, CommentSerializer



#AuthorList
class AuthorList(APIView):
    permission_classes = ()

    @swagger_auto_schema(responses = {200: AuthorSerializer(many = True)})
    def get(self, request):
        authors = Author.objects.select_related("user").all()
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
# class CategoryList(APIView):
#     permission_classes = ()
#
#     @swagger_auto_schema(responses = {200: CategorySerializer(many = True)})
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many = True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         """Создание категории"""
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryList(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

#CategoryCreate
class CategoryCreate(CreateAPIView):
    serializer_class = CategorySerializer



# class PostList(APIView):
#     permission_classes = ()
#
#     @swagger_auto_schema(responses = {200: PostSerializer(many = True)})
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many = True)
#         return Response(serializer.data)
#
# #     def post(self, request):
# #         serializer = PostSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostCreate(CreateAPIView):
    serializer_class = PostSerializer


#CommentList
class CommentList(APIView):
    permission_classes = ()

    @swagger_auto_schema(responses = {200: CommentSerializer(many = True)})
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many = True)
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