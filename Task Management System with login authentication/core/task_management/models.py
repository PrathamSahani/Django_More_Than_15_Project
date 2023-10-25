from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    task_image = models.ImageField(upload_to="receipe")
    task_view_count = models.PositiveIntegerField(default=1)
