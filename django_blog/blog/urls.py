from django.urls import path
from .views import (
    register,
    profile,
    CustomLoginView,
    CustomLogoutView,
    PostListCreateView,
    PostDetailView,
)

urlpatterns = [
    # Blog posts
    path("posts/", PostListCreateView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    # Authentication
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
]