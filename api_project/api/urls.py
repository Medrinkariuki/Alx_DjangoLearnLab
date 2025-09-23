from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, sample_api, BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Router for full CRUD
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', home, name='home'),
    path('api/sample/', sample_api, name='sample_api'),
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # token retrieval
    path('', include(router.urls)),  # include all CRUD routes
]