from rest_framework import serializers

from adverts.serializers import UserSerializer
from events.models import Event, EventComment
from users.models import Connect4ProUser


class EventCommentSerializer(serializers.ModelSerializer):
    '''Event comment serialize'''
    user = UserSerializer()
    class Meta:
        model = EventComment
        fields = ['id', 'post', 'text', 'user', 'posted']

    def create(self, validated_data):
        user = dict(validated_data.pop('user'))['id']
        post = validated_data['post']
        user = Connect4ProUser.objects.get(id=user)
        post = Event.objects.get(id=post.id)
        text = validated_data['text']
        comment = EventComment.objects.create(user=user, text=text, post=post)
        comment.save()
        return comment


class EventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    comments = EventCommentSerializer(source='post_comment', many=True)
    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'time', 'location', 'event_format', 'sum', 'event_image', 'description',
                  'comments']
        depth = 1
