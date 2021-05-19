from django.db import models

# Create your models here.

class Event(models.Model):
    """Мероприятие (тема, дата, время, сумма (вход))"""
    picture = models.ImageField()
    name = models.CharField(max_length = 100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length = 100)
    sum = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'