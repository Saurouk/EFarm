# blog/urls.py
from django.urls import path
from .views import BlogListView  # Exemple de vue à importer

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
]