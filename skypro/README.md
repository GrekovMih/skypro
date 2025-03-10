# Проект: Django-приложение для управления товарами

## Описание
Этот проект представляет собой Django-приложение для управления товарами. Он включает в себя аутентификацию пользователей, отображение таблицы товаров, админ-панель и поддержку статики через Docker.

## Функционал
- Регистрация и авторизация пользователей
- Отображение списка товаров с категориями и количеством заказов
- Админ-панель для управления товарами
- Защищённый доступ к данным (только для авторизованных пользователей)
- Docker и docker-compose для удобного развертывания


## Установка и запуск

1. **Клонировать репозиторий:**
   ```bash
   git clone https://github.com/username/project.git
   cd project
   ```

2. **Создать виртуальное окружение и установить зависимости:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Создать и применить миграции:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Создать суперпользователя (необязательно):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Запустить сервер:**
   ```bash
   python manage.py runserver
   ```

## Запуск с Docker

1. **Собрать и запустить контейнеры:**
   ```bash
   docker-compose up --build
   ```

2. **Остановить контейнеры:**
   ```bash
   docker-compose down
   ```


## Структура проекта
```
project/
│── core/             # Основные настройки Django
│── accounts/         # Приложение для аутентификации
│── products/         # Приложение для управления товарами
│── static/           # Статические файлы (CSS, JS)
│── templates/        # HTML-шаблоны
│── Dockerfile        # Конфигурация Docker
│── docker-compose.yml # Конфигурация Docker Compose
│── manage.py         # Django CLI
│── requirements.txt  # Список зависимостей
│── README.md         # Документация
```

