# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create sample authors
        self.author1 = Author.objects.create(name="J.R.R. Tolkien")
        self.author2 = Author.objects.create(name="George Orwell")

        # Create sample books
        self.book1 = Book.objects.create(
            title="The Hobbit",
            author=self.author1,
            publication_year=1937
        )
        self.book2 = Book.objects.create(
            title="1984",
            author=self.author2,
            publication_year=1949
        )

        # URLs for reverse lookups
        self.books_list_url = reverse('book-list-create')  # List & Create
        self.book_detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})  # Retrieve/Update/Delete

    # List Books
    def test_list_books(self):
        response = self.client.get(self.books_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Retrieve Book
    def test_retrieve_book(self):
        response = self.client.get(self.book_detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "The Hobbit")

    # Create Book (authenticated)
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {
            "title": "Animal Farm",
            "author": self.author2.pk,
            "publication_year": 1945
        }
        response = self.client.post(self.books_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # Create Book (unauthenticated)
    def test_create_book_unauthenticated(self):
        data = {
            "title": "Animal Farm",
            "author": self.author2.pk,
            "publication_year": 1945
        }
        response = self.client.post(self.books_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Update Book (authenticated)
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        data = {
            "title": "The Hobbit - Updated",
            "author": self.author1.pk,
            "publication_year": 1937
        }
        response = self.client.put(self.book_detail_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "The Hobbit - Updated")

    # Delete Book (authenticated)
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.book_detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # Filtering
    def test_filter_books(self):
        response = self.client.get(self.books_list_url, {'publication_year': 1937})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "The Hobbit")

    # Searching
    def test_search_books(self):
        response = self.client.get(self.books_list_url, {'search': 'Hobbit'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "The Hobbit")

    # Ordering
    def test_order_books(self):
        response = self.client.get(self.books_list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1949)
