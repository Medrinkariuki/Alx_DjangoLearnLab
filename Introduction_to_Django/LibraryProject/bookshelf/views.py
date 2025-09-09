from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    output = ", ".join([f"{book.title} by {book.author}" for book in books])
    return HttpResponse(output)