# Generated by Django 5.1.4 on 2025-01-25 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=250, verbose_name="Заголовок статьи"),
                ),
                ("content", models.TextField(verbose_name="Содержание статьи")),
                (
                    "preview",
                    models.ImageField(upload_to="images/", verbose_name="Изображение"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                ("published", models.BooleanField(null=True)),
                ("views_count", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
                "ordering": ["-created_at"],
            },
        ),
    ]
