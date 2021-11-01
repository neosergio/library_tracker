from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from library.models import Library, Book


class BookTestCase(TestCase):

    def test_book_creation(self):
        client = APIClient()
        book = {'title': 'A greatLibraryBookSerializer book',
                'author_name': 'A great authoLibraryBookSerializerr',
                'isbn_num': '123456',
                'genre': 'drama',
                'description': 'A great description for a great book'}
        response = client.post(
            '/api/v1/books/',
            book,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LibraryBookTestCase(TestCase):

    def setUp(self):
        library = Library(
            name='A amazing library',
            city='NY',
            state='NY',
            postal_code='10001'
        )
        library.save()
        book = Book(
            title='Another great book',
            author_name='A great author',
            isbn_num='123123',
            genre='novel',
            description='A great description'
        )
        book.save()
        self.library = library
        self.book = book

    def test_library_book_creation(self):
        client = APIClient()
        record_library_book = {
            "library": self.library.pk,
            "book": self.book.pk
        }
        response = client.post(
            '/api/v1/library_books/',
            record_library_book,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
