from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

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


class Grant(models.Model):
    grant_name = models.CharField(max_length=50, verbose_name='Имя гранта')
    grant_sum = models.PositiveIntegerField(verbose_name='Сумма гранта',
                                            validators=[MinValueValidator(1000), MaxValueValidator(10000000)])
    currency = models.CharField(max_length=5, default=kgs, choices=CURRENCY_CHOICES, verbose_name='Валюта')
    grant_deadline = models.CharField(max_length=20, verbose_name='Срок гранта')
    grant_description = models.TextField(max_length=300, verbose_name='Описание гранта')
    location = models.CharField(max_length=60, verbose_name='Локация', blank=True, null=True)
    period = models.CharField(max_length=25, verbose_name='Периодичность', choices=PERIOD_CHOICES, default=no)

    def __str__(self):
        return self.grant_name

    class Meta:
        verbose_name = 'Грант'
        verbose_name_plural = 'Гранты'


class Investment(models.Model):
    invest_name = models.CharField(max_length=50, verbose_name='Имя инвестиции')
    invest_sum = models.PositiveIntegerField(verbose_name='Сумма инвестиции',
                                             validators=[MinValueValidator(1000), MaxValueValidator(10000000)])
    currency = models.CharField(max_length=5, default=kgs, choices=CURRENCY_CHOICES, verbose_name='Валюта')
    invest_deadline = models.CharField(max_length=20, verbose_name='Срок инвестиции')
    invest_description = models.TextField(max_length=300, verbose_name='Описание инвестиции')
    location = models.CharField(max_length=60, verbose_name='Локация', blank=True, null=True)
    period = models.CharField(max_length=25, verbose_name='Периодичность', choices=PERIOD_CHOICES, default=no)

    def __str__(self):
        return self.invest_name

    class Meta:
        verbose_name = 'Инвестиция'
        verbose_name_plural = 'Инвестиции'


class GrantComment(models.Model):
    commentator_text = models.TextField(max_length=500, verbose_name='Ваш комментарий')
    commentator_name = models.CharField(max_length=50, verbose_name='Ваше имя')
    commentator_email = models.EmailField(verbose_name='Ваш контактный адрес почты')
    grant = models.ForeignKey(Grant, verbose_name='Грант', on_delete=models.CASCADE, related_name='grant_comment')

    def __str__(self):
        return f'Имя: {self.commentator_name}, контактная почта: {self.commentator_email}'

    class Meta:
        verbose_name = 'Комментарий гранта'
        verbose_name_plural = 'Комментарии грантов'


class InvestmentComment(models.Model):
    commentator_text = models.TextField(max_length=500, verbose_name='Ваш комментарий')
    commentator_name = models.CharField(max_length=50, verbose_name='Ваше имя')
    commentator_email = models.EmailField(verbose_name='Ваш контактный адрес почты')
    investment = models.ForeignKey(Investment, verbose_name='Инвестиция', on_delete=models.CASCADE,
                                   related_name='invest_comment')

    def __str__(self):
        return f'Имя: {self.commentator_name}, контактная почта: {self.commentator_email}'

    class Meta:
        verbose_name = 'Комментарий инвестиции'
        verbose_name_plural = 'Комментарии инвестиций'
