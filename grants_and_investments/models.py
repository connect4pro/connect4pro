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



class Grant(models.Model):
    grant_name = models.CharField(max_length = 50, verbose_name = 'Имя гранта')
    grant_sum = models.PositiveIntegerField(verbose_name = 'Сумма гранта', validators=[MinValueValidator(1000), MaxValueValidator(10000000)])
    currency = models.CharField(max_length = 5, default = kgs, choices = CURRENCY_CHOICES, verbose_name = 'Валюта')
    grant_deadline = models.CharField(max_length = 20, verbose_name = 'Срок гранта')
    grant_description = models.TextField(max_length = 300, verbose_name = 'Описание гранта')

    def __str__(self):
        return self.grant_name

    class Meta:
        verbose_name = 'Грант'
        verbose_name_plural = 'Гранты'

    


class Investment(models.Model):
    invest_name = models.CharField(max_length = 50, verbose_name = 'Имя инвестиции')
    invest_sum = models.PositiveIntegerField(verbose_name = 'Сумма инвестиции', validators=[MinValueValidator(1000), MaxValueValidator(10000000)])
    currency = models.CharField(max_length = 5, default = kgs, choices = CURRENCY_CHOICES, verbose_name = 'Валюта')
    invest_deadline = models.CharField(max_length = 20, verbose_name = 'Срок инвестиции')
    invest_description = models.TextField(max_length = 300, verbose_name = 'Описание инвестиции')

    def __str__(self):
        return self.invest_name

    class Meta:
        verbose_name = 'Инвестиция'
        verbose_name_plural = 'Инвестиции'


class GrantInvestmentComment(models.Model):
    commentator_text = models.TextField(max_length = 500, verbose_name = 'Ваш комментарий')
    commentator_name = models.CharField(max_length = 50, verbose_name = 'Ваше имя')
    commentator_email = models.EmailField(verbose_name = 'Ваш контактный адрес почты')

    def __str__(self):
        return f'Имя: {self.commentator_name}, контактная почта: {self.commentator_email}'

    class Meta:
        verbose_name = 'Комментарий гранта/инвестиции'
        verbose_name_plural = 'Комментарии грантов/инвестиций'