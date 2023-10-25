from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Shedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    subject_name = models.CharField(max_length=100)
    subject_description = models.TextField()
    class_link = models.CharField(max_length=500, default = 500)
    class_view_count = models.PositiveIntegerField(default=1)
