# user/serializers.py
from rest_framework import serializers
from .models import Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('username', 'email', 'numero_de_telephone', 'password')
        extra_kwargs = {'password': {'write_only': True}}  # Assurez-vous que le mot de passe n'est pas renvoyé dans les réponses

    def create(self, validated_data):
        utilisateur = Utilisateur(
            username=validated_data['username'],
            email=validated_data['email'],
            numero_de_telephone=validated_data['numero_de_telephone']
        )
        utilisateur.set_password(validated_data['password'])  # Hash du mot de passe
        utilisateur.save()
        return utilisateur
