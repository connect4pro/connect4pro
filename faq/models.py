from django.db import models
from django.db.models.base import Model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class WriteUs(models.Model):
    """Модель для отправки сообщения через форму обратной связи"""
    full_name = models.CharField(max_length = 50)
    phone = PhoneNumberField()
    email = models.EmailField()
    message = models.TextField(max_length = 300)

    class Meta:
        verbose_name = 'Сообщение от пользователя'
        verbose_name_plural = 'Сообщения от пользователей'

    def __str__(self):
        return self.full_name



class QuestionsAndAnswers(models.Model):
    """Модель, предназначенная для основных вопросов и ответов"""
    question = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 255)

    class Meta:
        verbose_name = 'Вопрос - ответ'
        verbose_name_plural = 'Вопросы и ответы'

    def __str__(self):
        return 'Вопрос: ' + self.question + ' Ответ: ' + self.answer