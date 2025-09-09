from .models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    # Get the author object
    author = Author.objects.get(name=author_name)
    # Get all books written by that author
    books = Book.objects.filter(author=author)
    return books

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian