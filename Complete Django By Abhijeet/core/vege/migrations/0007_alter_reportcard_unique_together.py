# Generated by Django 4.2.5 on 2023-09-27 09:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vege", "0006_reportcard"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="reportcard",
            unique_together={("student_rank", "date_of_report_card_generation")},
        ),
    ]
