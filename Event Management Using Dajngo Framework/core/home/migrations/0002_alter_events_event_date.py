# Generated by Django 4.2.6 on 2023-10-22 05:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="event_date",
            field=models.TextField(),
        ),
    ]