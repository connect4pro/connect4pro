from django.db import models


class TelegramCategory(models.Model):
    category = models.CharField(max_length=150, verbose_name='Категория чатов', unique=True)

    class Meta:
        verbose_name = 'Категория чатов'
        verbose_name_plural = 'Категории чатов'

    def __str__(self):
        return self.category


class TelegramLinks(models.Model):
    category = models.OneToOneField(TelegramCategory, verbose_name='Категория', related_name='link_category',
                                    on_delete=models.CASCADE)
    ru_link = models.URLField(max_length=200, verbose_name='Чат на русском', default=None)
    kg_link = models.URLField(max_length=200, verbose_name='Чат на кыргызском', default=None)

    class Meta:
        verbose_name = 'Ссылка на чат'
        verbose_name_plural = 'Ссылки на чаты'

    def __str__(self):
        return f'Ru: {self.ru_link} - Kg: {self.kg_link}'