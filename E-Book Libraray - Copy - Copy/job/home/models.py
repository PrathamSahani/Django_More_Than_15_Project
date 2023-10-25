from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models import *


# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add = True)
    
    class Meta:
        abstract = True
        
class BookCategory(BaseModel):
    category_name = models.CharField(max_length=100)
    
class Book(BaseModel):
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name="pizzas")
    book_name = models.CharField(max_length=100)
    price = models.IntegerField(default=100)
    images = models.CharField(max_length=500)
    
class Cart(BaseModel):
    user = models.ForeignKey(User, null=True, blank=True,  on_delete=models.SET_NULL, related_name="carts")
    is_paid = models.BooleanField(default=False)
    
    
class CartItems(BaseModel):
    cart =models.ForeignKey(Cart, on_delete=models.CASCADE, related_name = "cart_items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
