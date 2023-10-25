from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()
    event_date = models.IntegerField()
    event_view_count = models.PositiveIntegerField(default=1)
