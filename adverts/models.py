from django.db import models
from django_resized import ResizedImageField

usd = 'USD'
som = 'Сом'

CURRENCY_CHOICES = (
    (usd, 'USD'),
    (som, 'Сом'),
)

yes = 'Да'
no = 'Нет'
left = 'Оставить'
COMPLETE_CHOICES = (
    (yes, 'Да'),
    (no, 'Нет'),
    (left, 'Оставить')
)


class Category(models.Model):
    """Категория объявления"""

    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class UserAdvert(models.Model):
    """Объявление от пользователя"""

    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='advert_category')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=9, default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=usd, blank=True)
    completed = models.CharField(max_length=8, choices=COMPLETE_CHOICES, default=no)
    skills = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Запрос от пользователя'
        verbose_name_plural = 'Запросы от пользователей'


class BlogPost(models.Model):
    """Запись в блоге"""

    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    post_image = ResizedImageField(size=[350, 250], upload_to=f'images/blog_images/{title}-%d%m%Y', blank=True,
                                   null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Запись в блоге'
        verbose_name_plural = 'Записи в блоге'