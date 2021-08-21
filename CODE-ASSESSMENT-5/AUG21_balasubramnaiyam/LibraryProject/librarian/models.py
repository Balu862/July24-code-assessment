from django.db import models
from django.db.models.base import Model
# Create your models here.
class LibrarianModel(models.Model):
    enroll_code=models.IntegerField(default=None)
    name=models.CharField(max_length=50,default=None)
    address=models.CharField(max_length=50,default=None)
    mobilenumber=models.BigIntegerField(default=None)
    username=models.CharField (max_length=50,default=None)
    password=models.CharField(max_length=50,default=None)