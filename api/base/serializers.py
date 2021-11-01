from django.contrib.auth.models import User
from rest_framework import serializers

from library.models import Library, Book, LibraryBook, LibraryActivity


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class LibraryBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryBook
        fields = '__all__'


class LibraryActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryActivity
        fields = '__all__'
