# user/views.py
from rest_framework import generics
from .serializers import UtilisateurSerializer

class UtilisateurCreateView(generics.CreateAPIView):
    serializer_class = UtilisateurSerializer
