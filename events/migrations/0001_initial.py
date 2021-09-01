# Generated by Django 3.2 on 2021-09-01 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя мероприятия')),
                ('date', models.DateField(verbose_name='Дата мероприятия')),
                ('time', models.TimeField(verbose_name='Начало')),
                ('location', models.CharField(max_length=100, verbose_name='Место')),
                ('event_format', models.CharField(choices=[('Оффлайн', 'Оффлайн'), ('Онлайн', 'Онлайн')], default='Оффлайн', max_length=7, verbose_name='Формат мероприятия')),
                ('sum', models.PositiveIntegerField(verbose_name='Стоимость входа')),
                ('event_image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1024, 540], upload_to='images/event_images/%d%m%Y', verbose_name='Плакат мероприятия')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='EventComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Ваш комментарий')),
                ('posted', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='events.event', verbose_name='Объявление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_commenter', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий мероприятия',
                'verbose_name_plural': 'Комментарии мероприятий',
            },
        ),
    ]
