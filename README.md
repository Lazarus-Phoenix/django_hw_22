# Проект Skystore
---
![Screenshot 2025-01-26 at 05-19-06 AudioMarket · Bootstrap v5.3.png]()
![Screenshot 2025-01-26 at 05-22-03 AudioMarket · Bootstrap v5.3.png]()
![Screenshot 2025-01-26 at 05-23-09 AudioMarket · Bootstrap v5.3.png]()
![Screenshot 2025-01-26 at 05-24-34 AudioMarket · Bootstrap v5.3.png]()
---
Этот проект был разработан как домашнее задание с использованием фреймворка Django. 
Он включает в себя приложение каталога с домашней страницей и страницей контактов.

## Используемые технологии

- **Django**: Фреймворк для веб-разработки
- **Bootstrap**: Библиотека для стилей frontend
- **Python**: Язык программирования
- **Git**: Система управления версиями

## Структура проекта

django_hw_22/ 

│ ├── config/ <br>
│....├── init.py <br>
│....├── settings.py <br>
│....└── wsgi.py <br>
│ ├── blog/ <br>
│.......├──management/ <br>
│...........├──init.py <br>
│...........├──commands/ <br>
│...............├──init.py <br>
│....├──migrations/ <br>
│....├── init.py <br>
│....├── admin.py <br>
│....├── apps.py <br>
│....├── models.py <br>
│....├── tests.py <br>
│....└── views.py <br>
│....├── templates/ <br>
│ ├── catalog/ <br>
│.......├──management/ <br>
│...........├──init.py <br>
│...........├──commands/ <br>
│...............├──init.py <br>
│....├──migrations/ <br>
│....├── init.py <br>
│....├── admin.py <br>
│....├── apps.py <br>
│....├── models.py <br>
│....├── tests.py <br>
│....└── views.py <br>
│....├── templates/ <br>
│........├── home.html <br>
│........├── base.html <br>
│........├── product_detail.html <br>
│........├── product_list.html <br>
│........└── contacts.html <br>
│ └── static/ <br>
....└── css/ <br>
........└── bootstrap.min.css<br>



## Реализованные функции

1. **Домашняя страница**: Каталог товаров с фото и краткими описаниями
2. **Страница контактов**: Предоставляет детали контактов и форму для отправки сообщений

## Инструкции по настройке

1. Клонируйте этот репозиторий
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте виртуальное окружение:
   - На Windows: `venv\Scripts\activate`
   - На macOS/Linux: `source venv/bin/activate`
4. Установите зависимости: `pip install -r requirements.txt`
5. Либо poetry install если вам так удобнее.

## Запуск проекта

1. Перейдите в директорию проекта: `cd django_hw_22`
2. Запустите сервер разработки Django: `python3 manage.py runserver`

## Конфигурация URL

URL-адреса конфигурируются в файлах `django_hw_22/urls.py` и `catalog/urls.py`.

## Статические файлы

Статические файлы (CSS) хранятся в директории `static/css/`.

## Git Flow

- Основная ветка: `main`
- Ветка разработки: `develop`
- Ветки для задач: Именованы в соответствии с конкретными задачами (например, `feature/home-page`, `feature/contacts-page`)

## Лицензия

Этот проект является открытым и лицензируется по MIT.