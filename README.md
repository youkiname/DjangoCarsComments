# DjangoCarsComments
Реализация REST API для управления отзывами на автомобили. Используемые технологии: Django и DjangoRestFramework.

# How to run

### Set your database settings
1. Copy default_database_config.py to database_config.py
2. Replace db_name and db_user to your data
```
DATABASE_NAME = 'db_name'
DATABASE_USER = 'db_user'
DATABASE_PASSWORD = 'password'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'
```
3. Create database tables
```
python manage.py migrate
```

### Install requirements
1. Python 3.11+
2. Install pip requirements
```
pip install -r requirements.txt
```

### Run server
```
python manage.py runserver
```
