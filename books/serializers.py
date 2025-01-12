from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id','title', 'author', 'isbn', 'rating', 'coverUrl','isRead', 'notes')