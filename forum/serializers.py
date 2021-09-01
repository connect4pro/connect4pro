from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from forum.models import Author, Category, Post, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'fullname', 'bio']
        read_only_fields = ('slug',)


# class CategorySerializer(serializers.ModelSerializer):
#     title = serializers.CharField(required = True)
#
#     class Meta:
#         model = Category
#         fields = ['id', 'title', 'slug']
#         read_only_fields = ('slug',)
#
#
# class PostSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required = False)
#     category = CategorySerializer()
#
#     class Meta:
#         model = Post
#         fields = ['id', 'user', 'title', 'content', 'category']
#         read_only_fields = ('slug',)
#
#     def create(self, validated_data):
#         category = dict(validated_data.pop('category'))['title']
#         category = Category.objects.get(title = category)
#         new_post = Post.objects.create(category = category, user = validated_data['user'], title = validated_data['title'], content = validated_data['content'])
#         new_post.save()
#         return new_post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content']
        depth = 1


class CategorySerializer(serializers.ModelSerializer):

    posts = PostSerializer(source='post_category',many=True)



    def create(self, validated_data):
        category = Category.objects.get(id=validated_data['id'])
        posts_data = validated_data.pop['posts']

        for post in posts_data:
            post_obj = Post.objects.create(user=post['user'], title=post['title'], content=post['content'],
                                           category=category)
            post_obj.save()
        return category

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'posts']
        read_only_fields = ('slug',)
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id',)
