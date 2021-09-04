from patients import models
from patients.models import PatientModel
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientModel
        fields=('patient_code','name','address','phone','email','pincode','password')