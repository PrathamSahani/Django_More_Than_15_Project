# Generated by Django 4.2.6 on 2023-10-12 10:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_rename_pizza_name_book_book_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartitems",
            old_name="pizza",
            new_name="book",
        ),
    ]
