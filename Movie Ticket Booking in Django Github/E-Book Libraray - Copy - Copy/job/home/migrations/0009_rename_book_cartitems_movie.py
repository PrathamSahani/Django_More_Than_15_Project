# Generated by Django 4.2.6 on 2023-10-14 07:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0008_rename_bookcategory_moviecategory"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartitems",
            old_name="book",
            new_name="movie",
        ),
    ]
