# Generated by Django 5.1.6 on 2025-02-16 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name"],
                "permissions": [
                    ("can_unpublish_product", "Can unpublish product"),
                    ("can_delete_product", "Can delete product"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
