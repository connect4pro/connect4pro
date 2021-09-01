# Generated by Django 3.2 on 2021-09-01 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='Настоящее имя')),
                ('slug', models.SlugField(blank=True, max_length=400, unique=True)),
                ('bio', models.TextField(max_length=150, verbose_name='Немного о себе')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название категории')),
                ('slug', models.CharField(blank=True, max_length=400, unique=True)),
                ('description', models.TextField(verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Имя поста')),
                ('slug', models.SlugField(blank=True, max_length=400, unique=True)),
                ('content', models.TextField(max_length=300, verbose_name='Содержание поста')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.category', verbose_name='Категория поста')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.author', verbose_name=' Имя юзера, создающий пост')),
            ],
            options={
                'verbose_name': 'Пост автора на форуме',
                'verbose_name_plural': 'Посты авторов на форуме',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Ваш комментарий')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_comment', to='forum.comment', verbose_name='Комментарий к другому комментарию')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.post', verbose_name='Комментарии к посту')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.author', verbose_name='Юзер, которому вы напишите комментарий')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
