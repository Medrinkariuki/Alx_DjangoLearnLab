# api/views.py

from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Homepage view
def home(request):
    return HttpResponse("Welcome to API Project!")

# Sample API endpoint
def sample_api(request):
    data = {
        "message": "This is a sample API response",
        "status": "success"
    }
    return JsonResponse(data)

# DRF ListAPIView for books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# DRF ModelViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for the Book model:
    list, create, retrieve, update, destroy
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer