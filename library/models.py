from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'libraries'


class Book(models.Model):
    title = models.CharField(max_length=250)
    author_name = models.CharField(max_length=250)
    isbn_num = models.CharField(max_length=13)
    genre = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class LibraryBook(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    last_library_actity = models.OneToOneField('LibraryActivity', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.library.name} - {self.book.title}'


class LibraryActivity(models.Model):
    ACTIVITY_CHOICES = (
        ("CHECKIN", "checking-in"),
        ("CHECKOUT", "checking-out"),
    )
    activity_type = models.CharField(max_length=8,
                                     choices=ACTIVITY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library_book = models.ForeignKey(LibraryBook, on_delete=models.CASCADE)
    checked_out_at = models.DateTimeField(blank=True, null=True)
    checked_in_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.activity_type} - {self.library_book} - {self.user.username}'

    class Meta:
        verbose_name_plural = 'Library Activities'
