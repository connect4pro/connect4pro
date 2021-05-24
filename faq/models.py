from django.db import models
from django.db.models.base import Model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class WriteUs(models.Model):
    """Модель для отправки сообщения через форму обратной связи"""
    full_name = models.CharField(max_length = 50, verbose_name = 'Фамилия, имя, отчество')
    phone = PhoneNumberField(verbose_name = 'Контактный номер телефона')
    email = models.EmailField(verbose_name = 'Контактный адрес почты')
    message = models.TextField(max_length = 300, verbose_name = 'Ваше сообщение')

    class Meta:
        verbose_name = 'Сообщение от пользователя'
        verbose_name_plural = 'Сообщения от пользователей'

    def __str__(self):
        return self.full_name



class QuestionsAndAnswers(models.Model):
    """Модель, предназначенная для основных вопросов и ответов"""
    question = models.CharField(max_length = 100, verbose_name = 'Вопрос')
    answer = models.CharField(max_length = 255, verbose_name = 'Ответ')

    class Meta:
        verbose_name = 'Вопрос - ответ'
        verbose_name_plural = 'Вопросы и ответы'

    def __str__(self):
        return 'Вопрос: ' + self.question + ' Ответ: ' + self.answer