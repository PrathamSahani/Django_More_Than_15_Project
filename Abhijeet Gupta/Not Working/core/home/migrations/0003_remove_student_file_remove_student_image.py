# Generated by Django 4.2.5 on 2023-09-17 09:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_alter_student_address"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="file",
        ),
        migrations.RemoveField(
            model_name="student",
            name="image",
        ),
    ]
