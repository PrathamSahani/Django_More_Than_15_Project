# Generated by Django 4.2.5 on 2023-10-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExcelFile",
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
                ("file", models.FileField(upload_to="excel")),
            ],
        ),
    ]
