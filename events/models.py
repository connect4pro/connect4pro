from django.db import models
from django_resized import ResizedImageField
# Create your models here.

offline = 'Оффлайн'
online = 'Онлайн'

EVENT_FORMAT_CHOICES = (
    (offline, 'Оффлайн'),
    (online, 'Онлайн'),
    )

class Event(models.Model):
    """Мероприятие (тема, дата, время, сумма (вход))"""
    name = models.CharField(max_length = 100, verbose_name = 'Имя мероприятия')
    date = models.DateField(verbose_name = 'Дата мероприятия')
    time = models.TimeField(verbose_name = 'Начало')
    location = models.CharField(max_length = 100, verbose_name = 'Место')
    event_format = models.CharField(max_length = 7, default = offline, choices = EVENT_FORMAT_CHOICES, verbose_name = 'Формат мероприятия')
    sum = models.PositiveIntegerField(verbose_name = 'Стоимость входа')
    event_image = ResizedImageField(size=[250, 250], upload_to=f'images/event_images/{name}-%d%m%Y', blank=True,
                                   null=True, verbose_name = 'Плакат мероприятия')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'