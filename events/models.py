from django.db import models
from django_resized import ResizedImageField

# Create your models here.
from users.models import Connect4ProUser

offline = 'Оффлайн'
online = 'Онлайн'

EVENT_FORMAT_CHOICES = (
    (offline, 'Оффлайн'),
    (online, 'Онлайн'),
)


class Event(models.Model):
    """Мероприятие (тема, дата, время, сумма (вход))"""
    name = models.CharField(max_length=100, verbose_name='Имя мероприятия')
    date = models.DateField(verbose_name='Дата мероприятия')
    time = models.TimeField(verbose_name='Начало')
    location = models.CharField(max_length=100, verbose_name='Место')
    event_format = models.CharField(max_length=7, default=offline, choices=EVENT_FORMAT_CHOICES,
                                    verbose_name='Формат мероприятия')
    sum = models.PositiveIntegerField(verbose_name='Стоимость входа')
    event_image = ResizedImageField(size=[1024, 540], upload_to=f'images/event_images/%d%m%Y', blank=True,
                                    null=True, verbose_name='Плакат мероприятия')
    description = models.CharField(verbose_name='Описание', max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class EventComment(models.Model):
    text = models.TextField(max_length=500, verbose_name='Ваш комментарий')
    user = models.ForeignKey(Connect4ProUser, on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='event_commenter')
    post = models.ForeignKey(Event, verbose_name='Объявление', on_delete=models.CASCADE,
                             related_name='event_comment')
    posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Имя: {self.user.email}'

    class Meta:
        verbose_name = 'Комментарий мероприятия'
        verbose_name_plural = 'Комментарии мероприятий'
