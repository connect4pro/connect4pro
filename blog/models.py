from django.db import models

# Create your models here.
from django_resized import ResizedImageField


class BlogPost(models.Model):
    """Запись в блоге"""

    title = models.CharField(max_length=100)
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
    commentator_text = models.TextField(max_length=500, verbose_name='Комментарий')
    commentator_name = models.CharField(max_length=50, verbose_name='Имя')
    commentator_email = models.EmailField(verbose_name='Контактный адрес почты')
    post = models.ForeignKey(BlogPost, verbose_name='Блог', on_delete=models.CASCADE, related_name='blog_comment')

    def __str__(self):
        return f'Имя: {self.commentator_name}, - {self.commentator_email}'

    class Meta:
        verbose_name = 'Комментарий блога'
        verbose_name_plural = 'Комментарии блога'
