from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blood1(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blood1_name = models.CharField(max_length=100)
    blood1_description = models.TextField()
    blood1_reason = models.CharField(max_length=100, default='name')
    blood1_age = models.CharField(max_length=100, default='name')
    blood1_fill = models.CharField(max_length=100, default='name')
    blood1_status = models.CharField(max_length=100, default='Pending', null=True, blank=True)
  
    
class Blood(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blood_name = models.CharField(max_length=100)
    blood_description = models.TextField()
    blood_date = models.CharField(max_length=100, default='name')
    blood_status = models.CharField(max_length=100, default='pending', null=True, blank=True)
    blood_age = models.CharField(max_length=100, default='name')
    blood_fill = models.CharField(max_length=100, default='name')
    
    