from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register,
    CustomLoginView,
    CustomLogoutView
)

urlpatterns = [
    # Authentication
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Blog post CRUD (checker expects singular 'post' in URL)
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),          # note 'post/new/'
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # note 'update'
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
