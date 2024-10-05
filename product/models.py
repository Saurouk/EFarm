# product/models.py
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('agriculture', 'Produits agricoles'),
        ('outillages', 'Outils'),
        ('machines', 'Machines'),
    ]

    nom = models.CharField(max_length=255)
    quantite = models.PositiveIntegerField()
    prix_par_kg = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    categorie = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='images/products/', blank=True, null=True)  # Champ pour l'image

    def __str__(self):
        return self.nom
