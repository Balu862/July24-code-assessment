from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import StudentModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields=('id','name','address','class1','mobile','username','password')