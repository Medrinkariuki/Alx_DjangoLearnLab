from django.shortcuts import render
from .models import Book  # make sure this points to your Book model

def list_books(request):
    # Get all books
    books = Book.objects.all()
    
    # Render the template at relationship_app/list_books.html
    return render(request, "relationship_app/list_books.html", {"books": books})