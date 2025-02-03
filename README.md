# Проект Skystore
---
Добавляю тестовый товар 
![Screenshot 2025-02-03 at 08-52-20 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-03%20at%2008-52-20%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
![Screenshot 2025-02-03 at 08-47-49 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-03%20at%2008-47-49%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
Захожу в детализацию выставленного через форму тестового товара
![Screenshot 2025-02-03 at 08-48-31 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-03%20at%2008-48-31%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
Выбираю удалить и проваливаюсь в подтверждение выбора
![Screenshot 2025-02-03 at 08-49-00 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-03%20at%2008-49-00%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
Нет тестового товара после удаления
![Screenshot 2025-02-03 at 08-49-26 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-03%20at%2008-49-26%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
Отучиваем формы от плохих слов
![Screenshot 2025-02-03 at 08-53-45 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-03%20at%2008-53-45%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
Отучиваем формы от нереальных цен
![Screenshot 2025-02-03 at 08-54-29 AudioMarket · Bootstrap v5.3.png](static/HW_26_1_forms/Screenshot%202025-02-03%20at%2008-54-29%20AudioMarket%20%C2%B7%20Bootstrap%20v5.3.png)
## CRUD Создание редактирование обновление статей и удаление с формой выставления товара по предписанным признакам!

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
