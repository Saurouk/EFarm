# blog/urls.py
from django.urls import path
from .views import BlogListView, CreateBlogPostView  # Importation de la vue de création

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('create/', CreateBlogPostView.as_view(), name='blog-create'),  # URL pour la création d'un article
]
