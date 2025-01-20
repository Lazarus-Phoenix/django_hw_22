from django.db import models

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
        related_name='products'
    )
    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    update_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']  # Представление в админке сортированным по имени

    def __str__(self):
        return self.name


