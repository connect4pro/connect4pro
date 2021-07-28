from rest_framework import serializers
from events.models import Event, EventComment


class EventCommentSerializer(serializers.ModelSerializer):
    '''Event comment serialize'''

    class Meta:
        model = EventComment
        fields = ['id', 'post', 'text', 'user']


class EventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'date', 'time', 'location', 'event_format', 'sum', 'event_image', 'description',
                  'event_comment']
        depth = 1
