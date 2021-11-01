from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from library.models import Library, Book, LibraryBook, LibraryActivity
from .serializers import (
    UserSerializer,
    LibrarySerializer,
    BookSerializer,
    LibraryBookSerializer,
    LibraryActivitySerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class LibraryBookViewSet(viewsets.ModelViewSet):
    queryset = LibraryBook.objects.all()
    serializer_class = LibraryBookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LibraryActivityViewSet(viewsets.ModelViewSet):
    queryset = LibraryActivity.objects.all()
    serializer_class = LibraryActivitySerializer

    @action(detail=False, methods=['get'], url_path=r'user/(?P<user_pk>\d+)/books/checked-out')
    def list_books_checked_out_to_a_user(self, request, user_pk=None):
        user = get_object_or_404(User, pk=user_pk)
        books_checkout_by_user = LibraryActivity.objects.filter(user=user, activity_type="CHECKOUT")
        serializer = self.get_serializer(books_checkout_by_user, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'library/(?P<library_pk>\d+)/books/checked-out')
    def list_books_checked_out_to_a_library(self, request, library_pk=None):
        library = get_object_or_404(Library, pk=library_pk)
        books_checkout_by_library = LibraryActivity.objects.filter(
            library_book__library=library,
            activity_type="CHECKOUT")
        serializer = self.get_serializer(books_checkout_by_library, many=True)
        return Response(serializer.data)
