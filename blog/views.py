from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import BlogPostSerializer, BlogCommentSerializer
from blog.models import BlogPost, BlogComment


class BlogPostList(APIView):
    """
    Записи в блоге
    """
    permission_classes = ()

    @swagger_auto_schema(responses={200: BlogPostSerializer(many=True)})
    def get(self, request):
        posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)


class BlogDetail(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'id'


class BlogCommentsList(ListAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer


class BlogCommentCreate(CreateAPIView):
    serializer_class = BlogCommentSerializer
