from django.db.models import fields
from rest_framework import serializers
from librarian.models import LibrarianModel

class LibrarianSerializer(serializers.Serializer):
    class Meta:
        model=LibrarianModel
        fields=('name','address','mobilenumber', 'username', 'password')
