from django.db import models

from users.models import CustomUser

PUBLICATION_STATUS_CHOICES = [
    ('unpublished', 'Не опубликован'),
    ('draft', 'Черновик'),
    ('pending_review', 'Ожидает проверки'),
    ('published', 'Опубликован'),
]


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="catalog/product_images", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="catalog")
    purchase_price = models.FloatField(verbose_name="Цена товара", help_text="Введите цену товара")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    publication_status = models.CharField(max_length=20, choices=PUBLICATION_STATUS_CHOICES, default='unpublished')
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Владелец', help_text='Укажите владельца')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]

        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product"),
        ]

    def save(self, *args, **kwargs):
        self.full_clean()  # Вызывает все методы валидации модели
        super().save(*args, **kwargs)
