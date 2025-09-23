# api/views.py

from django.http import HttpResponse, JsonResponse
from rest_framework import generics
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
