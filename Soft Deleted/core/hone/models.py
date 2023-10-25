from django.db import models

# Create your models here.

class NonDeleted(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted= False)
    
    

class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)
    
    
    everything = models.Manager()
    objects = NonDeleted()
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()
        
    def restore(self):
        self.is_deleted = False
        self.save()
        
        
    class Meta:
        abstract = True
        
class Color(SoftDelete):
    color_name = models.CharField(max_length=100)
    color_hex_code = models.CharField(max_length=100)
    
    
    def __str__(self) -> str:
        return self.color_name