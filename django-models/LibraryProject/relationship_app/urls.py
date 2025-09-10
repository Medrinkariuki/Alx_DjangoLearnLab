from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),         # List all books
    path('add_book/', views.add_book, name='add_book'),    # Add a new book
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # Edit a book
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),  # Delete a book
]