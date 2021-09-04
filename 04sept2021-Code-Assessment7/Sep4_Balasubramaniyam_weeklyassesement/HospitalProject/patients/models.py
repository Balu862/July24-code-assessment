from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class PatientModel(models.Model):
    patient_code=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    pincode=models.IntegerField()
    password=models.CharField(max_length=50,default=None)



    
