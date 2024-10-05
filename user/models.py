# user/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UtilisateurManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse e-mail doit être fournie.')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class Utilisateur(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, verbose_name="Nom d'utilisateur")
    email = models.EmailField(unique=True, verbose_name="Adresse e-mail")
    password = models.CharField(max_length=128, verbose_name="Mot de passe")
    numero_de_telephone = models.CharField(max_length=15, verbose_name="Numéro de téléphone")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'  # Champ utilisé pour l'authentification
    REQUIRED_FIELDS = ['username']  # Champs requis pour la création d'un superutilisateur

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.username
