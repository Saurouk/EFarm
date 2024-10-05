# user/urls.py
from django.urls import path
from .views import UtilisateurCreateView

urlpatterns = [
    path('inscription/', UtilisateurCreateView.as_view(), name='utilisateur-inscription'),  # URL pour l'enregistrement des utilisateurs
]
