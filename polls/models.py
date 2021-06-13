from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# class Question(models.Model):
#     """Вопрос"""
#     title = models.CharField(max_length=200, verbose_name = "Вопрос")
#     max_points = models.FloatField(default = 100, verbose_name = "Макс.процент")

#     class Meta:
#         verbose_name = 'Вопрос'
#         verbose_name_plural = 'Вопросы'
 
#     def __str__(self):
#         return self.title
 
# class Answer(models.Model):
#     """Варианты ответов"""
#     answers = models.FloatField(default = 0, verbose_name = "Варианты ответов")

#     def __str__(self):
#         return f'{self.answers}'

#     class Meta:
#         verbose_name = 'Вариант ответа'
#         verbose_name_plural = 'Варианты ответа'

# class Result(models.Model):
#     """Результаты теста"""
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "ФИО тестируемого")
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name = "Вопрос")
#     user_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name = "Ответ")
#     datetime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name = "Время завершения теста")

#     def __str__(self):
#         return f'{self.user_answer}'

#     class Meta:
#         verbose_name = 'Результат'
#         verbose_name_plural = 'Результаты'

class Question(models.Model):
    title = models.CharField(max_length=4096)
    visible = models.BooleanField(default=True)
    max_points = models.FloatField(default = 100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    points = models.FloatField()
    lock_other = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.points}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice.points}'

    class Meta:
        verbose_name = 'Ответы пользователя'
        verbose_name_plural = 'Ответы пользователей'