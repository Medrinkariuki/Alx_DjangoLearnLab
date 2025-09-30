from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentUpdateView,
    CommentDeleteView,
    add_comment,        # function-based view for creating comments
    TagPostListView,
    search_posts,
)

urlpatterns = [
    # Post URLs
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # Comment URLs
    path("post/<int:pk>/comment/", add_comment, name="add-comment"),   # create comment
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

    # Tag and Search URLs
    path("tags/<slug:slug>/", TagPostListView.as_view(), name="posts-by-tag"),
    path("search/", search_posts, name="search-posts"),
]