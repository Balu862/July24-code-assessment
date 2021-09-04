from django.db import models

# Create your models here.
class DoctorsModel(models.Model):
    doctor_code=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    specialization=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)



    
