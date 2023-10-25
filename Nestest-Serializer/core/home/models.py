from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)
 