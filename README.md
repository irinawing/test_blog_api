# 📝 Test Blog API

[![Django](https://img.shields.io/badge/Django-4.x-success)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/DRF-3.14+-informational)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-blue)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## О проекте

**Test Blog API** — это учебный проект для создания и управления записями блога через REST API.

Реализован на Django и Django Rest Framework с поддержкой базы данных PostgreSQL.

---

## Технологии

- Python 3.11
- Django 4.x
- Django Rest Framework 3.14+
- PostgreSQL 14+
- SQLite (для локальной разработки)

---

## Установка и запуск

```bash
git clone https://github.com/irinawing/test_blog_api.git
cd test_blog_api
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Для использования PostgreSQL:**

1. Установите PostgreSQL.
2. Создайте базу данных и пользователя.
3. Обновите настройки подключения в `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

4. Примените миграции:

```bash
python manage.py migrate
```

---

## Документация API

Доступна по адресам:

- `http://127.0.0.1:8000/api/schema/swagger/` — Swagger UI
- `http://127.0.0.1:8000/api/schema/redoc/` — ReDoc

---

## Контакты

Автор: [irinawing](https://github.com/irinawing)

