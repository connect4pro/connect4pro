from django.db import models

# Create your models here.
from django_resized import ResizedImageField

from users.models import Connect4ProUser


class BlogPost(models.Model):
    """Запись в блоге"""

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    post_image = ResizedImageField(size=[350, 250], upload_to=f'images/blog_images/%d%m%Y', blank=True,
                                   null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Запись в блоге'
        verbose_name_plural = 'Записи в блоге'


class BlogComment(models.Model):
    text = models.TextField(max_length=500, verbose_name='Ваш комментарий')
    user = models.ForeignKey(Connect4ProUser, on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='blog_commenter')
    post = models.ForeignKey(BlogPost, verbose_name='Объявление', on_delete=models.CASCADE,
                             related_name='post_comment')
    posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Имя: {self.user.email}'

    class Meta:
        verbose_name = 'Комментарий блога'
        verbose_name_plural = 'Комментарии блога'
