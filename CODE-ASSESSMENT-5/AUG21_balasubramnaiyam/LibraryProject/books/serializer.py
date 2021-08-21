from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from books.models import BookModel

class BookSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=BookModel
        fields=('bookname','author','description','publisher','price')
        #,'author',