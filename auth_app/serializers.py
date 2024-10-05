# auth_app/serializers.py
from rest_framework import serializers
from user.models import Utilisateur

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'username', 'email', 'password', 'numero_de_telephone']
        extra_kwargs = {
            'password': {'write_only': True}  # Rendre le mot de passe uniquement en écriture
        }



    def create(self, validated_data):
        user = Utilisateur(**validated_data)
        user.set_password(validated_data['password'])  # Hachage du mot de passe
        user.save()
        return user
