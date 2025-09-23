from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, sample_api, BookList, BookViewSet

# Create router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', home, name='home'),
    path('api/sample/', sample_api, name='sample_api'),
    path('books/', BookList.as_view(), name='book-list'),  # ListAPIView
    path('', include(router.urls)),  # Include all CRUD routes from the router
]
