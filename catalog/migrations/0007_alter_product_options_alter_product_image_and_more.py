# Generated by Django 5.1.6 on 2025-02-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name"],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="catalog/product_images"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="publication_status",
            field=models.CharField(
                choices=[
                    ("unpublished", "Не опубликован"),
                    ("draft", "Черновик"),
                    ("pending_review", "Ожидает проверки"),
                    ("published", "Опубликован"),
                ],
                default="unpublished",
                max_length=20,
            ),
        ),
    ]
