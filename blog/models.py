from django.db import models

# Create your models here.
from django_resized import ResizedImageField


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