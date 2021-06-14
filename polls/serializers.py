from django.db.models import fields
from rest_framework import serializers
from .models import Question, Choices, GetPoll

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question',]
        read_only = ('id',)

class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = ['id', 'option_count',]
        read_only = ('id',)

class GetPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetPoll
        fields = ['question_id', 'choose_option',]
        read_only = ('id',)

        