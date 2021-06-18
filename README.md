`python -m venv venv` - установка окружения

`pip install requirements.txt` - для установки зависимостей

База данных - **PostgreSQL** - пароли пока что записаны в `settings.py`

запуск celery-beat - `celery -A connect4pro beat`

запуск воркера celery - `celery -A connect4pro worker -l info -Ofair --pool=solo`

Предварительно установить Redis и запустить.

