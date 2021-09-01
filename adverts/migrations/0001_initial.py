# Generated by Django 3.2 on 2021-09-01 07:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Набор изображений',
                'verbose_name_plural': 'Наборы изображений',
            },
        ),
        migrations.CreateModel(
            name='BusinessAdvert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена')),
                ('currency', models.CharField(blank=True, choices=[('USD', 'USD'), ('Сом', 'Сом')], default='USD', max_length=3, verbose_name='Валюта')),
                ('completed', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет'), ('Оставить', 'Оставить')], default='Нет', max_length=8, verbose_name='Завершено')),
                ('needs', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Мне нужно')),
                ('suggest', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Я предлагаю')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Объявление МСБ',
                'verbose_name_plural': 'Объявления МСБ',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Категория')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ProviderAdvert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена')),
                ('currency', models.CharField(blank=True, choices=[('USD', 'USD'), ('Сом', 'Сом')], default='USD', max_length=3, verbose_name='Валюта')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('location', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('scope', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('services', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('foundation_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Дата основания')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_advert_category', to='adverts.category', verbose_name='Категория')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_set', to='adverts.album', verbose_name='Фото')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_profile', to='users.providerprofile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Объявление провайдера',
                'verbose_name_plural': 'Объявления провайдеров',
            },
        ),
        migrations.CreateModel(
            name='ProviderAdvertComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Ваш комментарий')),
                ('posted', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='adverts.provideradvert', verbose_name='Объявление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_commenter', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий объявления консультанта',
                'verbose_name_plural': 'Комментарии объявлений консультантов',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[350, 250], upload_to='images/adverts/%d%m%Y')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='adverts.album')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessAdvertComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Ваш комментарий')),
                ('posted', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='adverts.businessadvert', verbose_name='Объявление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_commenter', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий объявления МСБ',
                'verbose_name_plural': 'Комментарии объявлений МСБ',
            },
        ),
        migrations.AddField(
            model_name='businessadvert',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_advert_category', to='adverts.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='businessadvert',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_profile', to='users.businessprofile', verbose_name='Пользователь'),
        ),
    ]
