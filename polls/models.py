from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Question(models.Model):
    question = models.CharField(max_length = 200, verbose_name = 'Вопрос')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Choices(models.Model):
    option_count = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name = 'Балл за вариант ответа')

    def __str__(self):
        return f'{self.option_count}'

class GetPoll(models.Model):
    question_id = models.ForeignKey(Question, on_delete = models.DO_NOTHING)
    choose_option = models.ForeignKey(Choices, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.question_id} + {self.choose_option}'