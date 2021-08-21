from django.db import models

# Create your models here.
class BookModel(models.Model):
    bookname=models.CharField(max_length=50)
    author=models.CharField(max_length=50,default=None)
    description=models.CharField(max_length=50,default=None)
    publisher=models.CharField(max_length=50,default=None)
    price=models.IntegerField(default=None)