from django.db.models import fields
from rest_framework import serializers
from faq.models import WriteUs, QuestionsAndAnswers

class WriteUsSerializer(serializers.ModelSerializer):
    """WriteUs serialize"""
    class Meta:
        model = WriteUs
        fields = '__all__'


class QuestionsAndAnswersSerializer(serializers.ModelSerializer):
    """QuestionsAndAnswers serialize"""
    class Meta:
        model = QuestionsAndAnswers
        fields = '__all__'