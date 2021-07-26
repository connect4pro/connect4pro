from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.db.models import Sum, Avg

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


class Question(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Вопрос")
    # possible_answer = models.IntegerField(choices = ANSWER_CHOICES, verbose_name = "Вариант ответа")

    def __str__(self):
        return self.title


class ResultPoll(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    # questions = models.ForeignKey(Question, on_delete = models.CASCADE, verbose_name = "Вопрос пользователю")
    # answers = models.ForeignKey(Answer, on_delete = models.CASCADE, verbose_name = "Ответ пользователя")
    date_pass_poll = models.DateTimeField(auto_now_add = True)
    avg_points = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.avg_points}'



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