from django.urls import path
from .views import (
    BlogPostListCreateView,
    BlogPostDetailView,
    CommentListCreateView,
    CommentDetailView,
    CategoryListView,
    TagListView,
    ReactionListCreateView,
    RegisterView,
    LoginView,
)

urlpatterns = [
    path('blog-posts/', BlogPostListCreateView.as_view(), name='blog-post-list-create'),
    path('blog-posts/<int:pk>/', BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list-create'),
    path('tags/', TagListView.as_view(), name='tag-list-create'),
    path('reactions/', ReactionListCreateView.as_view(), name='reaction-list-create'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
