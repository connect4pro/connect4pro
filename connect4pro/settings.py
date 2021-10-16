"""
Django settings for connect4pro project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

from django.template.context_processors import media
from dotenv import load_dotenv

SITE_ID = 1
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')
# TODO: Закрыть доступ для посторонних айпи

ALLOWED_HOSTS = ['http://localhost:8000', 'http://localhost:3000', 'http://94.228.120.61/', 'http://94.228.120.61',
                 '94.228.120.61', '127.0.0.1', 'http://cj28902.tmweb.ru', 'http://connect4.pro', 'connect4.pro',
                 'cj28902.tmweb.ru', 'https://customer.paybox.money', 'https://api.paybox.money', 'api.paybox.money']

# Application definition

INSTALLED_APPS = [

    # Apps
    'adverts.apps.AdvertsConfig',
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'events.apps.EventsConfig',
    'faq.apps.FaqConfig',
    'grants_and_investments.apps.GrantsAndInvestmentsConfig',
    'forum.apps.ForumConfig',
    'polls.apps.PollsConfig',
    'newsletter.apps.NewsletterConfig',
    'payments.apps.PaymentsConfig',
    'social_auth.apps.SocialAuthConfig',
    'testimage.apps.TestimageConfig',

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'rest_framework_simplejwt',
    'drf_yasg',
    'phonenumber_field',
    # 'tinymce',
    # 'hitcount',
    # 'taggit',
    'rest_framework_serializer_field_permissions',
    'pytils',
    'social_django',
    'corsheaders',
    'django_rest_passwordreset',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'connect4pro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'connect4pro.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

try:
    import pymysql

    pymysql.version_info = (1, 4, 6, 'final', 0)
    pymysql.install_as_MySQLdb()
except:
    pass

# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get('ENGINE'),
#         'NAME': os.environ.get('NAME'),
#         'USER': os.environ.get('USER'),
#         'PASSWORD': os.environ.get('PASSWORD'),
#         'HOST': os.environ.get('HOST'),
#         'PORT': os.environ.get('PORT'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('NAME'),
        'USER': os.environ.get('DBUSER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': os.environ.get('MSQL_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/c/cj28902/public_html/static/'
REACT_APP = os.path.join(BASE_DIR, 'frontend')
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/c/cj28902/public_html/media/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'frontend/static'),
# )


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

PHONENUMBER_DB_FORMAT = 'INTERNATIONAL'
PHONENUMBER_DEFAULT_REGION = 'KG'

AUTH_USER_MODEL = 'users.Connect4ProUser'
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    "django.contrib.auth.backends.ModelBackend",
)
SWAGGER_SETTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
}

# SOCIAL_AUTH_POSTGRES_JSONFIELD = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
FIELDS_STORED_IN_SESSION = ['user_type']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'locale': 'ru_RU',
    'fields': 'name, email'
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
            'redirect_uri': 'http://connect4.pro/<custom-url>'
        }
    }
}
# LOGIN_REDIRECT_URL = '/api/token'
# LOGOUT_REDIRECT_URL = '/api/token'

# SOCIAL_AUTH_PIPELINE = (
#     'users.pipelines.create_user',    # custom method
#
# )

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'connect4fund@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_IMPORTS = [
    'newsletter.tasks',
]

PAYBOX_KEY = os.environ.get('PAYBOX_KEY')

CORS_ALLOWED_ORIGINS = [
    'http://94.228.120.61',
    'http://localhost:3000',
    'http://localhost:8000',
    'http://127.0.0.1:3000',
    'http://cj28902.tmweb.ru',
    'http://connect4.pro',
    'https://connect4.pro',
    'https://customer.paybox.money',
    'https://api.paybox.money',
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'FETCH',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://94.228.120.61',
    'http://94.228.120.61',
    'http://cj28902.tmweb.ru',
    'http://connect4.pro',
    'https://connect4.pro',
    'https://customer.paybox.money',
    'https://api.paybox.money',
)

DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_QUALITY = 100
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=36500),
}
CSRF_COOKIE_NAME = "XSRF-TOKEN"
CSRF_USE_SESSIONS = True

SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

BROKER_BACKEND = 'sqlakombu.transport.Transport'

SQLALCHEMY_DATABASE_URI = 'sqla+sqlite:////home/c/cj28902/celerydb.sqlite'
BROKER_HOST = 'sqla+sqlite:////home/c/cj28902/celerydb.sqlite'
BROKER_URL = 'sqla+sqlite:////home/c/cj28902/celerydb.sqlite'
