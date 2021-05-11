from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import BlogPostSerializer
from blog.models import BlogPost


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