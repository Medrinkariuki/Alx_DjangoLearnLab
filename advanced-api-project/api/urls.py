# api/urls.py

from django.urls import path
from .views import (
    BookListCreateView,
    BookRetrieveUpdateDestroyView,
    AuthorListCreateView,
    AuthorDetailView,
)

urlpatterns = [
    # Book endpoints
    path("books/", BookListCreateView.as_view(), name="book-list-create"),  # List & Create
    path("books/<int:pk>/", BookRetrieveUpdateDestroyView.as_view(), name="book-detail"),  # Retrieve, Update, Delete

    # Author endpoints
    path("authors/", AuthorListCreateView.as_view(), name="author-list-create"),  # List & Create
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),  # Retrieve, Update, Delete
]