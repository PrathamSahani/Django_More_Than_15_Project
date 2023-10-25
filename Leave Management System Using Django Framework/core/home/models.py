from django.db import models
from django.contrib.auth.models import User

# Create your models here.Events
class Leaves(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    leave_description = models.TextField()
    leave_date = models.IntegerField()
    leave_accept = models.CharField(max_length=100, null=True, blank=True)
    event_view_count = models.PositiveIntegerField(default=1)

