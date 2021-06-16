# Generated by Django 3.2.3 on 2021-06-16 12:41

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=300)),
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
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image_1', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[350, 250], upload_to='images/blog_images/%d%m%Y')),
                ('image_2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[350, 250], upload_to='images/blog_images/%d%m%Y')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('currency', models.CharField(blank=True, choices=[('USD', 'USD'), ('Сом', 'Сом')], default='USD', max_length=3)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_advert_category', to='adverts.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_profile', to='users.providerprofile')),
            ],
            options={
                'verbose_name': 'Объявление провайдера',
                'verbose_name_plural': 'Объявления провайдеров',
            },
        ),
        migrations.CreateModel(
            name='BusinessAdvert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('currency', models.CharField(blank=True, choices=[('USD', 'USD'), ('Сом', 'Сом')], default='USD', max_length=3)),
                ('completed', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет'), ('Оставить', 'Оставить')], default='Нет', max_length=8)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_advert_category', to='adverts.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_profile', to='users.businessprofile')),
            ],
            options={
                'verbose_name': 'Объявление МСБ',
                'verbose_name_plural': 'Объявления МСБ',
            },
        ),
    ]
