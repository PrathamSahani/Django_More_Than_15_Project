from django.db import models

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    hotel_descritption = models.TextField()
    created_at = models.DateField(auto_now_add =True)
    updated_at = models.DateField(auto_now  =True)
    
    def __str__(self) -> str:
        return self.hotel_name

    