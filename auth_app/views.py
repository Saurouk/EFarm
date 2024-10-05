# auth_app/views.py
from rest_framework import generics
from rest_framework.response import Response

from .serializers import UserSerializer
from user.models import Utilisateur

class UserCreateView(generics.CreateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    queryset = Utilisateur.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        # Modification des clés pour afficher en français
        response_data = [
            {
                "id": user['id'],
                "nom_utilisateur": user['username'],
                "adresse_email": user['email'],
                "num_telephone": user['numero_de_telephone'],
            } for user in serializer.data
        ]
        return Response(response_data)