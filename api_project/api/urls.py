from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # Homepage
    path('api/sample/', views.sample_api, name='sample_api'),  # Sample API
]