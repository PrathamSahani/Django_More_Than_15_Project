# Generated by Django 4.2.5 on 2023-10-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipe", "0006_remove_blood_blood_image_blood_blood_age_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blood",
            name="blood_age",
            field=models.CharField(default="name", max_length=100),
        ),
        migrations.AlterField(
            model_name="blood",
            name="blood_fill",
            field=models.CharField(default="name", max_length=100),
        ),
        migrations.AlterField(
            model_name="receipe",
            name="receipe_age",
            field=models.CharField(default="name", max_length=100),
        ),
        migrations.AlterField(
            model_name="receipe",
            name="receipe_fill",
            field=models.CharField(default="name", max_length=100),
        ),
    ]
