from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Расширенная модель пользователя Django.

    Эта модель расширяет стандартную модель User, добавляя дополнительные поля:
    - email: уникальный адрес электронной почты
    - phone_number: номер телефона
    - avatar: аватар пользователя
    - country: страна проживания
    - first_name: первое имя
    - last_name: фамилия
    - password1 и password2: пароли (используются для переопределения формы регистрации)

    USERNAME_FIELD указывает, что уникальным идентификатором пользователя является email.
    """

    email = models.EmailField(unique=True, verbose_name = 'Электронная почта' ,help_text='Уникальный адрес электронной почты пользователя.')
    """
    Уникальный адрес электронной почты пользователя.
    """

    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Номер телефона' ,help_text='Номер телефона пользователя. Можно оставить пустым.')
    """
    Номер телефона пользователя. Поле необязательное (blank=True, null=True).
    """

    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name = 'Аватарка' ,help_text='Аватар пользователя. Можно оставить пустым.')
    """
    Аватар пользователя. Поле необязательное (blank=True, null=True).
    """

    country = models.CharField(max_length=50, blank=True, null=True, verbose_name = 'Страна' ,help_text='Страна проживания пользователя. Можно оставить пустым.')
    """
    Страна проживания пользователя. Поле необязательное (blank=True, null=True).
    """

    first_name = models.CharField(max_length=150, blank=True, null=True, verbose_name = 'Имя', help_text='Имя пользователя.')
    """
    Имя пользователя.
    """

    last_name = models.CharField(max_length=150, blank=True, null=True, verbose_name = 'Фамилия' , help_text='Фамилия пользователя.')
    """
    Фамилия пользователя.
    """

    token = models.CharField(max_length=100, blank=True, null=True, verbose_name = "Token")

    USERNAME_FIELD = 'email'
    """
    Имя поля, которое используется как имя пользователя. В данном случае это поле 'email'.
    """

    REQUIRED_FIELDS = []  # Изменили REQUIRED_FIELDS
    """
    Список полей, которые должны быть заполнены при создании нового пользователя,
    помимо USERNAME_FIELD. Теперь включает first_name и last_name.
    """

    def __str__(self):
        """
        Строковое представление объекта CustomUser.
        Возвращает email пользователя.
        """
        return self.email

# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
#     country = models.CharField(max_length=50, blank=True, null=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     def __str__(self):
#         return self.email