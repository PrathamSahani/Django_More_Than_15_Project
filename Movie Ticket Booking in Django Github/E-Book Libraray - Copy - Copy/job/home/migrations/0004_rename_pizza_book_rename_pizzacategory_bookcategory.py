# Generated by Django 4.2.6 on 2023-10-12 10:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_alter_pizza_images"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Pizza",
            new_name="Book",
        ),
        migrations.RenameModel(
            old_name="PizzaCategory",
            new_name="BookCategory",
        ),
    ]