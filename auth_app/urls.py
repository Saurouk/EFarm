# auth_app/urls.py
from django.urls import path
from .views import UserCreateView, UserUpdateView, UserDeleteView, UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),  # Pour lister les utilisateurs
    path('users/create/', UserCreateView.as_view(), name='user-create'),  # Pour créer un nouvel utilisateur
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),  # Pour mettre à jour un utilisateur
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),  # Pour supprimer un utilisateur
]
