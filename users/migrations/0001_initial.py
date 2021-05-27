# Generated by Django 3.2.3 on 2021-05-26 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0013_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connect4ProUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('company_name', models.CharField(blank=True, max_length=100, verbose_name='Название компании')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Телефон/Telegram')),
                ('facebook', models.CharField(blank=True, max_length=50, verbose_name='Facebook')),
                ('instagram', models.CharField(blank=True, max_length=50, verbose_name='Instagram')),
                ('site', models.CharField(blank=True, max_length=50, verbose_name='Сайт')),
                ('is_premium', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Сектор деятельности',
                'verbose_name_plural': 'Секторы деятельности',
            },
        ),
        migrations.CreateModel(
            name='ProviderProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(blank=True, max_length=100, verbose_name='ФИО руководителя')),
                ('description', models.CharField(blank=True, max_length=300, verbose_name='Описание')),
                ('year', models.DateField(blank=True, verbose_name='Год основания')),
                ('logo', models.ImageField(blank=True, upload_to='images/provider/logo/%d%m%Y/', verbose_name='Логотип')),
                ('address', models.CharField(blank=True, default='', max_length=200, verbose_name='Адрес')),
                ('services', models.CharField(blank=True, max_length=200, verbose_name='Список услуг')),
                ('scope', models.CharField(blank=True, max_length=200, verbose_name='Сфера деятельности')),
                ('as_provider', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='provider_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль консультанта',
                'verbose_name_plural': 'Профили консультантов',
            },
        ),
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='Фамилия')),
                ('region', models.CharField(choices=[('Все', 'Весь Кыргызстан'), ('Чуй', 'Чуйская область'), ('Нарын', 'Нарынская область'), ('Баткен', 'Баткенская область'), ('Талас', 'Таласская область'), ('Ош', 'Ошская область'), ('Джалал-Абад', 'Джалал-Абадская область'), ('Иссык-Куль', 'Иссык-Кульская область')], default=1, max_length=30)),
                ('turnover', models.CharField(choices=[('до 100 000', 'до 100 000'), ('до 500 000', 'до 100 000'), ('до 1 000 000', 'до 1 000 000'), ('до 5 000 000', 'до 5 000 000'), ('до 10 000 000', 'до 10 000 000'), ('более 10 000 000', 'более 10 000 000')], default=1, max_length=20, verbose_name='Примерный оборот')),
                ('employers', models.PositiveSmallIntegerField(blank=True, default=1, verbose_name='Число сотрудников')),
                ('demand', models.CharField(blank=True, max_length=50, verbose_name='Ищу')),
                ('supply', models.CharField(blank=True, max_length=50, verbose_name='Предлагаю')),
                ('as_business', models.BooleanField(default=True)),
                ('sector', models.ManyToManyField(blank=True, to='users.Sector', verbose_name='Сектор деятельности')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='business_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
