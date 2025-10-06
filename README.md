# MyBlog — Django учебный проект

## О проекте
Простой блог на Django с CRUD для категорий и постов и приятным Bootstrap-дизайном.

## Быстрый старт
1. Создать виртуальное окружение и активировать:
   - Linux/macOS:
     ```
     python -m venv venv
     source venv/bin/activate
     ```
   - Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```

2. Установить зависимости:
```
pip install -r requirements.txt
```

3. Выполнить миграции и создать суперпользователя:
```
python manage.py migrate
python manage.py createsuperuser
```

4. Запустить сервер:
```
python manage.py runserver
```

Открой http://127.0.0.1:8000/

## Примечания
- Для создания/редактирования/удаления требуется авторизация. Можно войти в админку (http://127.0.0.1:8000/admin/) или реализовать регистрацию отдельно.
- В режиме DEBUG=True проект использует локальную SQLite базу `db.sqlite3`.
