from django.urls import path
from .views import home, sample_api, BookList

urlpatterns = [
    path('', home, name='home'),
    path('api/sample/', sample_api, name='sample_api'),
    path('api/books/', BookList.as_view(), name='book_list'),
]