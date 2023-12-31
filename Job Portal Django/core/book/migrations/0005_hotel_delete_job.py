# Generated by Django 4.2.6 on 2023-10-12 08:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0004_job_delete_hotel"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hotel",
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
                ("hotel_name", models.CharField(max_length=100)),
                ("hotel_description", models.TextField()),
                ("hotel_image", models.CharField(max_length=500)),
                ("price", models.IntegerField()),
                ("emenities", models.ManyToManyField(to="book.emenitites")),
            ],
        ),
        migrations.DeleteModel(
            name="Job",
        ),
    ]
