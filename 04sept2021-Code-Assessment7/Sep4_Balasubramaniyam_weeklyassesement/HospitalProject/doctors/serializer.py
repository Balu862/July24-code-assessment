from doctors import models
from doctors.models import DoctorsModel
from rest_framework import serializers

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorsModel
        fields=('doctor_code','name','address','mobile','email','specialization','password')