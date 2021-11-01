from django.contrib import admin

from .models import Library, Book, LibraryBook, LibraryActivity

# Register your models here.
admin.site.register(Library)
admin.site.register(Book)
admin.site.register(LibraryBook)
admin.site.register(LibraryActivity)
