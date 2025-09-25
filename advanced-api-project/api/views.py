from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# -----------------------------
# Book Views
# -----------------------------

class ListView(generics.ListAPIView):
    """
    Retrieves all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class DetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class CreateView(generics.CreateAPIView):
    """
    Creates a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
