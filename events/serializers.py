from rest_framework import serializers

from adverts.serializers import UserSerializer
from events.models import Event, EventComment


class EventCommentSerializer(serializers.ModelSerializer):
    '''Event comment serialize'''
    user = UserSerializer()
    class Meta:
        model = EventComment
        fields = ['id', 'post', 'text', 'user', 'posted']


class EventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    comments = EventCommentSerializer(source='post_comment', many=True)
    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'time', 'location', 'event_format', 'sum', 'event_image', 'description',
                  'comments']
        depth = 1
