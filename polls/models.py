from enum import unique
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.db.models import Sum, Avg
from phonenumber_field.modelfields import PhoneNumberField

from users.models import Connect4ProUser

User = get_user_model()

ANSWER_ONE = 0
ANSWER_TWO = 20
ANSWER_THREE = 40
ANSWER_FOUR = 60
ANSWER_FIVE = 80
ANSWER_SIX = 100

ANSWER_CHOICES = (
    (ANSWER_ONE, 0),
    (ANSWER_TWO, 20),
    (ANSWER_THREE, 40),
    (ANSWER_FOUR, 60),
    (ANSWER_FIVE, 80),
    (ANSWER_SIX, 100),
)
CLOSED = 'Закрыт'
OPENED = 'Открыт'
STATUS_CHOICES = (
    (CLOSED, 'Закрыт'),
    (OPENED, 'Открыт')
)

class Question(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Вопрос")
    # possible_answer = models.IntegerField(choices = ANSWER_CHOICES, verbose_name = "Вариант ответа")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Список вопросов"


class ResultPoll(models.Model):
    user = models.ForeignKey(Connect4ProUser, on_delete = models.CASCADE, null = True)
    # questions = models.ForeignKey(Question, on_delete = models.CASCADE, verbose_name = "Вопрос пользователю")
    # answers = models.ForeignKey(Answer, on_delete = models.CASCADE, verbose_name = "Ответ пользователя")
    date_pass_poll = models.DateTimeField(auto_now_add = True)
    avg_points = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.avg_points}'

    class Meta:
        verbose_name = "Результат опроса"
        verbose_name_plural = "Результаты опросов"

class СonsultationForm(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Имя")
    phone_number = PhoneNumberField(null = False, verbose_name = "Номер телефона")
    messanger = models.CharField(max_length = 30, verbose_name = "Whats'App или Telegram")

    def __str__(self):
        return f'{self.name}, {self.phone_number}, {self.messanger}'

    class Meta:
        verbose_name = "Обращение через форму для консультации"
        verbose_name_plural = "Все обращения через форму для консультаций"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE, verbose_name = "Вопрос пользователю")
    final_answer = models.IntegerField(choices = ANSWER_CHOICES, verbose_name = "Ответ пользователя")
    poll_result = models.ForeignKey(ResultPoll, on_delete = models.DO_NOTHING)
    def __str__(self):
        return f'{self.final_answer}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        average = self.poll_result.answer_set.all().aggregate(Avg('final_answer'))
        self.poll_result.avg_points = average['final_answer__avg']
        self.poll_result.save()


class Appeal(models.Model):
    result_poll = models.ForeignKey(ResultPoll, on_delete=models.CASCADE, verbose_name='Результат опроса')
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=16, verbose_name='Телеграм/WhatsApp')
    email = models.EmailField(verbose_name='email')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата обращения')
    status = models.CharField(max_length=20, verbose_name='Статус', choices=STATUS_CHOICES, default=OPENED, null=True)

    def __str__(self):
        return f'{self.email} - {self.date}'

    class Meta:
        verbose_name = 'Запрос консультации'
        verbose_name_plural = 'Запросы консультаций'
