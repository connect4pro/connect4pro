from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import tree
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
from pytils.translit import slugify
from django_resized import ResizedImageField
from django.shortcuts import reverse 
# Create your models here.

User = get_user_model()

class Author(models.Model):
    '''Модель пользователя форума'''
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Пользователь')
    fullname = models.CharField(max_length = 40, blank = True, verbose_name = 'Настоящее имя пользователя')
    slug = slug = models.SlugField(max_length = 400, unique = True, blank = True)
    bio = models.TextField(max_length = 150, verbose_name = 'Немного о себе')
    profile_pic = ResizedImageField(size = [50, 80], quality = 100, upload_to='authors', default = None, null = True, verbose_name = 'Изображение профиля')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.fullname


class Category(models.Model):
    '''Модель категории форума'''
    title = models.CharField(max_length = 50, verbose_name = 'Название категории')
    slug = models.CharField(max_length = 400, unique = True, blank = True)
    description = models.TextField(default = 'Описание категории:', verbose_name = 'Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('posts', kwargs = {
            'slug': self.slug
        })

    @property
    def num_posts(self):
        return Post.objects.filter(categories = self).count()

    @property
    def last_post(self):
        return Post.objects.filter(categories = self).latest('date')




class Reply(models.Model):
    '''Модель ответов комментаторам на форуме'''
    user = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name = 'Юзер, которому вы напишите комментарий')
    content = models.TextField(verbose_name = 'Комментарий')
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.content[:100]

    class Meta:
        verbose_name = 'Ответ комментатору'
        verbose_name_plural = 'Ответы комментаторам'



class Comment(models.Model):
    '''Модель ответов комментаторов автору поста на форуме'''
    user = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name = 'Юзер, которому вы напишите комментарий')
    content = models.TextField(verbose_name = 'Ваш комментарий')
    date = models.DateTimeField(auto_now_add = True)
    replies = models.ManyToManyField(Reply, blank = True, verbose_name = 'Комментарии других юзеров')

    def __str__(self):
        return self.content[:100]

    class Meta:
        verbose_name = 'Ответ автору поста'
        verbose_name_plural = 'Ответы авторам постов'




class Post(models.Model):
    '''Модель сообщений на форуме'''
    title = models.CharField(max_length = 400, verbose_name = 'Имя поста')
    slug = models.SlugField(max_length = 400, unique = True, blank = True)
    user = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name = ' Имя юзера, создающий пост')
    content = models.TextField(max_length = 300, verbose_name = 'Содержание поста')
    categories = models.ManyToManyField(Category, verbose_name = 'Категория поста')
    date = models.DateTimeField(auto_now_add = True)
    approved = models.BooleanField(default = False, verbose_name = 'Статус отправки поста')
    hit_count_generic = GenericRelation(HitCount, object_id_field = 'object_pk', related_query_name = 'hit_count_generic_relation')
    tags = TaggableManager(verbose_name = 'Тег поста')
    comments = models.ManyToManyField(Comment, blank = True, verbose_name = 'Комментарии юзеров к автору поста')

    @property
    def num_comments(self):
        return self.comments.count()

    @property
    def last_reply(self):
        return self.comments.latest('date')

    class Meta:
        verbose_name = 'Пост автора на форуме'
        verbose_name_plural = 'Посты авторов на форуме'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('detail', kwargs = {
            'slug': self.slug
        })