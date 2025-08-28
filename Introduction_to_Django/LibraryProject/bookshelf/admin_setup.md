# Django Admin Setup for Book Model

## Steps to Register Book Model in Admin

1. Open `bookshelf/admin.py`.
2. Add the following code:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')