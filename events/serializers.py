from rest_framework import serializers
from events.models import Event, EventComment


class EventSerializer(serializers.ModelSerializer):
    """Event serialize"""
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('user',)

class EventCommentSerializer(serializers.ModelSerializer):
    '''Event comment serialize'''
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = EventComment
        fields = '__all__'
        read_only_fields = ('user',)
