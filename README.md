python -m venv venv - установка окружения

pip install requirements.txt - для установки зависимостей

База данных - PostgreSQL - пароли пока что записаны в settings.py

python manage.py makemigrations - создание миграций

python manage.py migrate - применение миграций

python manage.py createsuperuser - создание суперпользователя (после применения первоначальных миграций)
просит ввести email и пароль с подтверждением

запуск celery-beat - celery -A connect4pro beat

запуск воркера celery - celery -A connect4pro worker -l info -Ofair --pool=solo

Предварительно установить Redis и запустить.

http://127.0.0.1:8000/swagger/ - документация API
