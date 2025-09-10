from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view (simple list of book titles and authors)
def book_list(request):
    books = Book.objects.all()
    output = ", ".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output)

# Class-based view (library detail with its books)
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()  # assuming related_name="books"
        return context
