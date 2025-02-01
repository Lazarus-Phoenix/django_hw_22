from django.db import models
from django import forms

from django.core.exceptions import ValidationError



"""
 Валидатор для проверки запрещенных слов
"""
from django.conf import settings

def validate_forbidden_words(value):
    forbidden_words = getattr(settings, 'FORBIDDEN_WORDS', [])
    value_lower = value.lower()
    for word in forbidden_words:
        if word in value_lower:
            raise ValidationError(f' Использование слова "{word}" запрещено.')


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(
        max_length=200
    )
    description = models.TextField()

    image = models.ImageField(
        upload_to='catalog/product_images',
        null=True,
        blank=True,
        verbose_name="Фото",
        help_text="Загрузите фото товара"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='catalog'
    )
    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    """
    Запомнить! валидация пишется сразу за полем self(ссылку) на которое и делает 
    """
    def clean(self):
        if self.purchase_price < 0:
            raise ValidationError("Цена не может быть отрицательной.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Вызывает все валидаторы, включая custom clean methods
        super().save(*args, **kwargs)



    created_at = models.DateTimeField(
        auto_now_add=True
    )
    update_at = models.DateTimeField(
        auto_now=True
    )

    # def clean(self):
    #     # Вызываем clean родительского класса
    #     super().clean()
    #
    #     # Применяем валидаторы к полям name и description
    #     validate_forbidden_words(self.name)
    #     validate_forbidden_words(self.description)
    #
    # def save(self, *args, **kwargs):
    #     self.full_clean()  # Вызывает все валидаторы, включая custom clean methods
    #     super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']  # Представление в админке сортированным по имени

    def __str__(self):
        return self.name


