# Generated by Django 4.2.5 on 2023-09-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vege", "0008_alter_reportcard_date_of_report_card_generation"),
    ]

    operations = [
        migrations.AddField(
            model_name="receipe",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]