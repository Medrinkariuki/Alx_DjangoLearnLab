# query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    """
    Returns a queryset of all books written by the author with the given name.
    """
    # Get the author object
    author = Author.objects.get(name=author_name)
    # Return all books that have this author
    return Book.objects.filter(author=author)

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    """
    Returns the librarian assigned to the library with the given name.
    """
    # Get the library object
    library = Library.objects.get(name=library_name)
    # Return the librarian assigned to this library
    return Librarian.objects.get(library=library)

# Optional: example usage for testing
if __name__ == "__main__":
    author_name = "J.K. Rowling"
    library_name = "Central Library"

    print("Books by author:", books_by_author(author_name))
    print("Librarian for library:", librarian_for_library(library_name))