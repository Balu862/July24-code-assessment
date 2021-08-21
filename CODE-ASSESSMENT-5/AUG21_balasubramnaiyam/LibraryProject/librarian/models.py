from django.db import models
from django.db.models.base import Model
# Create your models here.
class LibrarianModel(models.Model):
    enroll_code=models.IntegerField()
    name=models.CharField(max_length=50,default=None)
    address=models.CharField(max_length=50,default=None)
    mobilenumber=models.BigIntegerField()
    username=models.CharField (max_length=50)
    password=models.CharField(max_length=50)