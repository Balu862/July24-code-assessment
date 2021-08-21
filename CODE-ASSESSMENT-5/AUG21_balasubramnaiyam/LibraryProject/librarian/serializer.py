from django.db.models.base import Model
from rest_framework import fields, serializers
from librarian.models import LibrarianModel
 
class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model=LibrarianModel
        fields=("enroll_code","name","address","mobilenumber","username","password")