# Generated by Django 4.2.3 on 2023-10-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Color",
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
                ("is_deleted", models.BooleanField(default=False)),
                ("color_name", models.CharField(max_length=100)),
                ("color_hex_code", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
