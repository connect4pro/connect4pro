# Generated by Django 3.2 on 2021-08-31 13:32

from django.conf import settings
import django.core.validators
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
            name='Grant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя гранта')),
                ('sum', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(10000000)], verbose_name='Сумма гранта')),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('Сом', 'KGS'), ('Евро', 'EUR'), ('Рубль', 'RUB')], default='Сом', max_length=5, verbose_name='Валюта')),
                ('deadline', models.CharField(max_length=20, verbose_name='Срок гранта')),
                ('description', models.TextField(verbose_name='Описание гранта')),
                ('location', models.CharField(blank=True, max_length=60, null=True, verbose_name='Локация')),
                ('period', models.CharField(choices=[('Нет', 'Нет'), ('Постоянно', 'Постоянно'), ('Ежемесячно', 'Ежемесячно'), ('Ежегодно', 'Ежегодно'), ('Еженедельно', 'Еженедельно'), ('Раз в полгода', 'Раз в полгода'), ('Раз в несколько лет', 'Раз в несколько лет')], default='Нет', max_length=25, verbose_name='Периодичность')),
                ('logo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[52, 52], upload_to='images/grants/logo/%d%m%Y')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[520, 520], upload_to='images/grants/images/%d%m%Y')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Грант',
                'verbose_name_plural': 'Гранты',
            },
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя инвестиции')),
                ('sum', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(10000000)], verbose_name='Сумма инвестиции')),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('Сом', 'KGS'), ('Евро', 'EUR'), ('Рубль', 'RUB')], default='Сом', max_length=5, verbose_name='Валюта')),
                ('deadline', models.CharField(max_length=20, verbose_name='Срок инвестиции')),
                ('description', models.TextField(verbose_name='Описание инвестиции')),
                ('location', models.CharField(blank=True, max_length=60, null=True, verbose_name='Локация')),
                ('period', models.CharField(choices=[('Нет', 'Нет'), ('Постоянно', 'Постоянно'), ('Ежемесячно', 'Ежемесячно'), ('Ежегодно', 'Ежегодно'), ('Еженедельно', 'Еженедельно'), ('Раз в полгода', 'Раз в полгода'), ('Раз в несколько лет', 'Раз в несколько лет')], default='Нет', max_length=25, verbose_name='Периодичность')),
                ('logo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[52, 52], upload_to='images/invests/logo/%d%m%Y')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[520, 520], upload_to='images/invests/images/%d%m%Y')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Инвестиция',
                'verbose_name_plural': 'Инвестиции',
            },
        ),
        migrations.CreateModel(
            name='InvestmentComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Ваш комментарий')),
                ('posted', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='grants_and_investments.investment', verbose_name='Объявление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invest_commenter', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий инвестиции',
                'verbose_name_plural': 'Комментарии инвестиций',
            },
        ),
        migrations.CreateModel(
            name='GrantComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Ваш комментарий')),
                ('posted', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='grants_and_investments.grant', verbose_name='Объявление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grant_commenter', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий гранта',
                'verbose_name_plural': 'Комментарии грантов',
            },
        ),
    ]
