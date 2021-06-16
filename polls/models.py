from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.db.models import Sum, Avg

User = get_user_model()


class Question(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Вопрос")

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE, verbose_name = "Вопрос")
    possible_answer = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name = "Вариант ответа")

    def __str__(self):
        return f'{self.possible_answer}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE, verbose_name = "Вопрос пользователю")
    final_answer = models.ForeignKey(Choice, on_delete = models.CASCADE, verbose_name = "Ответ пользователя")

    def __str__(self):
        return f'{self.final_answer}'


class ResultPoll(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    questions = models.ForeignKey(Question, on_delete = models.CASCADE, verbose_name = "Вопрос пользователю")
    answers = models.ForeignKey(Answer, on_delete = models.CASCADE, verbose_name = "Ответ пользователя")
    date_pass_poll = models.DateTimeField(auto_now_add = True)
    avg_points = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.answers.final_answer}'