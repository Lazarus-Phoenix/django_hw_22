# Проект Skystore
---
![Screenshot 2025-02-11 at 04-58-41 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-11%20at%2004-58-41%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
![Screenshot 2025-02-11 at 04-59-21 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-11%20at%2004-59-21%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
![Screenshot 2025-02-11 at 04-59-45 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-11%20at%2004-59-45%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
## Регистрация с подтверждением проходом по ссылке отправляемой на почту
![Screenshot 2025-02-11 at 05-01-58 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-11%20at%2005-01-58%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
![Снимок экрана от 2025-02-11 05-03-38.png](static/HW_26_1_forms/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-02-11%2005-03-38.png)
## Страница приземления по ссылки из почты, уже доступна копка "Написать статью"
![Снимок экрана от 2025-02-11 05-04-08.png](static/HW_26_1_forms/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-02-11%2005-04-08.png)
## А в базе данных появляется user is_active
![Снимок экрана от 2025-02-11 05-09-06.png](static/HW_26_1_forms/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-02-11%2005-09-06.png)
![Снимок экрана от 2025-02-11 05-09-49.png](static/HW_26_1_forms/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202025-02-11%2005-09-49.png)
##user is_active и все страницы преобразились фунционалом "только для своих"- добавления товаров и написания статей
![Screenshot 2025-02-11 at 05-06-34 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-11%20at%2005-06-34%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
![Screenshot 2025-02-11 at 05-06-57 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-11%20at%2005-06-57%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
![Screenshot 2025-02-11 at 05-08-02 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-11%20at%2005-08-02%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)





## CRUD Создание редактирование обновление статей и удаление с формой выставления товара по предписанным признакам!

---
Реализованна регистрация пользователей, по ссылке отправляемой на почту указанной в 
форме регистрации, 
Так же введены ограничения к редактированию и публикации на сайте  для не зарегистрированных
пользователей.
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
│.......├── management/ <br>
│...........├── init.py <br>
│...........├── commands/ <br>
│...............├──init.py <br>
│....├── migrations/ <br>
│....├── init.py <br>
│....├── admin.py <br>
│....├── apps.py <br>
│....├── models.py <br>
│....├── templates/ <br>
│....├── tests.py <br>
│....└── views.py <br>
│
│ ├── catalog/ <br>
│.......├── management/ <br>
│...........├── init.py <br>
│...........├── commands/ <br>
│...............├── init.py <br>
│....├── migrations/ <br>
│....├── init.py <br>
│....├── admin.py <br>
│....├── apps.py <br>
│....├── forms.py <br>
│....├── models.py <br>
│....├── templates/ <br>
│....├── tests.py <br>
│....└── views.py <br>
│........├── home.html <br>
│........├── base.html <br>
│........├── product_create.html <br>
│........├── product_update.html <br>
│........├── product_delete_confirm.html <br>
│........├── product_detail.html <br>
│........├── product_list.html <br>
│........└── contacts.html <br>
│ ├── users/ <br>
│....├── migrations/ <br>
│....├── init.py <br>
│....├── admin.py <br>
│....├── apps.py <br>
│....├── forms.py <br>
│....├── models.py <br>
│....├── templates/ <br>
│....├── tests.py <br>
│....└── views.py <br>
│ └── static/ <br>
....└── css/ <br>
........└── bootstrap.min.css<br>

# Вся архитектура функционала сайта переведена с FBV на CBV
1. Реализованы шаблоны, шаблонные теги и фильтры
2. Реализована пагинация
3. Реализовано добавление продукта пользователем
4. Реализована страница продукта
5. На главной странице выводятся все продукты


## Реализованный функционал

1. **Домашняя страница**: Каталог товаров с фото и краткими описаниями
2. **Страница контактов**: Предоставляет детали контактов и форму для отправки сообщений
3. **Блог**: Блог с публикуемыми тематическими статьями отсортированными по дате, читайте свежее первым 
4. Регистрация , уровни доступа к функционалу в зависимости от регистрации
5. Задействован SMTP с отправкой сгенерированной ссылкой для верификации почты её владельцем  

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
