from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import *

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'final_answer']



class UserPollSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = True)
    email = serializers.CharField(required = True)

    class Meta:
        model = Connect4ProUser
        fields = ['id', 'email']


class ResultPollSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = True)
    user = UserPollSerializer()

    class Meta:

        model = ResultPoll
        fields = ['id', 'user', 'date_pass_poll', 'avg_points']

    def create(self, validated_data):
        user = dict(validated_data.pop('user'))['id']
        user = Connect4ProUser.objects.get(id = user)
        poll = ResultPoll.objects.create(user = user, avg_points = validated_data['avg_points'])
        poll.save()
        return poll

class ConsultationFormSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required = True)

    class Meta:
        model = СonsultationForm
        fields = ['id','name', 'phone_number', 'messanger']