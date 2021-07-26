from rest_framework import serializers
from events.models import Event, EventComment


class EventCommentSerializer(serializers.ModelSerializer):
    '''Event comment serialize'''
    id = serializers.IntegerField(read_only=True)
    event = serializers.IntegerField(required=True)

    class Meta:
        model = EventComment
        fields = '__all__'
        read_only_fields = ('user',)


class EventSerializer(serializers.ModelSerializer):
    """Event serialize"""
    id = serializers.IntegerField(read_only=True)
    comments = EventCommentSerializer(many=True)

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('user',)
