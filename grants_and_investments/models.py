from ckeditor.fields import RichTextField
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from django_resized import ResizedImageField

from users.models import Connect4ProUser

usd = 'USD'
kgs = 'Сом'
eur = 'Евро'
rub = 'Рубль'

CURRENCY_CHOICES = (
    (usd, 'USD'),
    (kgs, 'KGS'),
    (eur, 'EUR'),
    (rub, 'RUB'),
)

no = 'Нет'
permanent = 'Постоянно'
monthly = 'Ежемесячно'
yearly = 'Ежегодно'
weekly = 'Еженедельно'
half = 'Раз в полгода'
years = 'Раз в несколько лет'
PERIOD_CHOICES = (
    (no, 'Нет'),
    (permanent, 'Постоянно'),
    (monthly, 'Ежемесячно'),
    (yearly, 'Ежегодно'),
    (weekly, 'Еженедельно'),
    (half, 'Раз в полгода'),
    (years, 'Раз в несколько лет'),
)


class GrantTag(models.Model):
    name = models.CharField(max_length=150, verbose_name='Тег', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Grant(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя гранта/инвестиции')
    sum = models.CharField(verbose_name='Сумма гранта/инвестиции или другое', max_length=150, default='')
    currency = models.CharField(max_length=5, default=kgs, choices=CURRENCY_CHOICES, verbose_name='Валюта')
    deadline = models.CharField(max_length=20, verbose_name='Срок гранта/инвестиции', null=True, blank=True)
    description = RichTextField(verbose_name='Описание гранта/инвестиции')
    location = models.CharField(max_length=60, verbose_name='Локация', blank=True, null=True)
    period = models.CharField(max_length=25, verbose_name='Периодичность', choices=PERIOD_CHOICES, default=no)
    logo = ResizedImageField(size=[52, 52], upload_to=f'images/grants/logo/%d%m%Y', blank=True,
                             null=True)
    image = ResizedImageField(size=[520, 520], upload_to=f'images/grants/images/%d%m%Y', blank=True,
                              null=True)
    created_at = models.DateTimeField(auto_now=True)
    is_grant = models.BooleanField(verbose_name='Это грант', default=False)
    is_invest = models.BooleanField(verbose_name='Это инвестиция', default=False)
    tag = models.ManyToManyField(GrantTag, verbose_name='Теги', related_name='grant_tags')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Грант/Инвестиция'
        verbose_name_plural = 'Гранты/Инвестиции'


# class Investment(models.Model):
#     name = models.CharField(max_length=50, verbose_name='Имя инвестиции')
#     sum = models.PositiveIntegerField(verbose_name='Сумма инвестиции',
#                                       validators=[MinValueValidator(1000), MaxValueValidator(10000000)])
#     currency = models.CharField(max_length=5, default=kgs, choices=CURRENCY_CHOICES, verbose_name='Валюта')
#     deadline = models.CharField(max_length=20, verbose_name='Срок инвестиции')
#     description = RichTextField(verbose_name='Описание инвестиции')
#     location = models.CharField(max_length=60, verbose_name='Локация', blank=True, null=True)
#     period = models.CharField(max_length=25, verbose_name='Периодичность', choices=PERIOD_CHOICES, default=no)
#     logo = ResizedImageField(size=[52, 52], upload_to=f'images/invests/logo/%d%m%Y', blank=True,
#                              null=True)
#     image = ResizedImageField(size=[520, 520], upload_to=f'images/invests/images/%d%m%Y', blank=True,
#                               null=True)
#     created_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Инвестиция'
#         verbose_name_plural = 'Инвестиции'


class GrantComment(models.Model):
    text = models.TextField(max_length=500, verbose_name='Ваш комментарий')
    user = models.ForeignKey(Connect4ProUser, on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='grant_commenter')
    post = models.ForeignKey(Grant, verbose_name='Объявление', on_delete=models.CASCADE,
                             related_name='post_comment')
    posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Имя: {self.user.email}'

    class Meta:
        verbose_name = 'Комментарий гранта'
        verbose_name_plural = 'Комментарии грантов'

# class InvestmentComment(models.Model):
#     text = models.TextField(max_length=500, verbose_name='Ваш комментарий')
#     user = models.ForeignKey(Connect4ProUser, on_delete=models.CASCADE, verbose_name='Пользователь',
#                              related_name='invest_commenter')
#     post = models.ForeignKey(Investment, verbose_name='Объявление', on_delete=models.CASCADE,
#                              related_name='post_comment')
#     posted = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'Имя: {self.user.email}'
#
#     class Meta:
#         verbose_name = 'Комментарий инвестиции'
#         verbose_name_plural = 'Комментарии инвестиций'
