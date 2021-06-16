from django.db.models import fields
from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'possible_answer']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'final_answer']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'final_answer']

class ResultPollSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultPoll
        fields = ['id', 'user', 'questions', 'answers', 'date_pass_poll', 'avg_points']