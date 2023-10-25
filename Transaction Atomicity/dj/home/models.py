from django.db import models

class Payment(models.Model):
    user = models.CharField(max_length=100, unique=True)  # Fix the unique attribute
    amount = models.IntegerField(default=100)
