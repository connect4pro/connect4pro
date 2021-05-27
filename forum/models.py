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
# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    fullname = models.CharField(max_length = 40, blank = True)
    slug = slug = models.SlugField(max_length = 400, unique = True, blank = True)
    bio = models.TextField(max_length = 150)
    profile_pic = ResizedImageField(size = [50, 80], quality = 100, upload_to='authors', default = None, null = True)

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
    title = models.CharField(max_length = 50)
    slug = models.CharField(max_length = 400, unique = True, blank = True)

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
    title = models.CharField(max_length = 400)
    slug = models.SlugField(max_length = 400, unique = True, blank = True)
    user = models.ForeignKey(Author, on_delete = models.CASCADE)
    content = models.TextField(max_length = 300)
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add = True)
    approved = models.BooleanField(default = False)
    hit_count_generic = GenericRelation(HitCount, object_id_field = 'object_pk', related_query_name = 'hit_count_generic_relation')
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title