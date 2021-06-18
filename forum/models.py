from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import tree
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from pytils.translit import slugify
from django.shortcuts import reverse
# Create your models here.

User = get_user_model()

class Author(models.Model):
    '''Модель пользователя форума'''
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Пользователь')
    fullname = models.CharField(max_length = 50, verbose_name = 'Настоящее имя')
    slug = models.SlugField(max_length = 400, unique = True, blank = True)
    bio = models.TextField(max_length = 150, verbose_name = 'Немного о себе')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.fullname + f' ({self.user})'


class Category(models.Model):
    '''Модель категории форума'''
    title = models.CharField(max_length = 50, verbose_name = 'Название категории')
    slug = models.CharField(max_length = 400, unique = True, blank = True)
    description = models.TextField(verbose_name = 'Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    '''Модель постов на форуме'''
    user = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name = ' Имя юзера, создающий пост')
    title = models.CharField(max_length = 400, verbose_name = 'Имя поста')
    slug = models.SlugField(max_length = 400, unique = True, blank = True)
    content = models.TextField(max_length = 300, verbose_name = 'Содержание поста')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = 'Категория поста')
    date = models.DateTimeField(auto_now_add = True)
		
    def get_comments(self):
        return self.comment_set.filter(parent__isnull=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост автора на форуме'
        verbose_name_plural = 'Посты авторов на форуме'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    '''Модель комментариев на форуме'''
    user = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name = 'Юзер, которому вы напишите комментарий')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = 'Комментарии к посту')
    comment = models.TextField(verbose_name = 'Ваш комментарий')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name = 'Комментарий к другому комментарию', related_name = 'parent_comment')
    date = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.comment