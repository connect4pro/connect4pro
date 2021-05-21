from django.db import models

# Create your models here.
class Grant(models.Model):
    grant_name = models.CharField(max_length = 50, verbose_name = 'Имя гранта')
    grant_sum = models.PositiveIntegerField(verbose_name = 'Сумма гранта')
    grant_deadline = models.CharField(max_length = 20, verbose_name = 'Срок гранта')
    grant_description = models.TextField(max_length = 300, verbose_name = 'Описание гранта')

    def __str__(self):
        return self.grant_name

    class Meta:
        verbose_name = 'Грант'
        verbose_name_plural = 'Гранты'


class Investment(models.Model):
    invest_name = models.CharField(max_length = 50, verbose_name = 'Имя инвестиции')
    invest_sum = models.PositiveIntegerField(verbose_name = 'Сумма инвестиции')
    invest_deadline = models.CharField(max_length = 20, verbose_name = 'Срок инвестиции')
    invest_description = models.TextField(max_length = 300, verbose_name = 'Описание инвестиции')

    def __str__(self):
        return self.invest_name

    class Meta:
        verbose_name = 'Инвестиция'
        verbose_name_plural = 'Инвестиции'