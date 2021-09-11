from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    class1=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

