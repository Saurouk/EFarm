from django.contrib import admin
from django.utils.html import format_html
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prix_par_kg', 'image_apercu']

    # Méthode pour afficher l'aperçu de l'image dans l'admin
    def image_apercu(self, obj):
        if obj.produit_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.produit_image.url)
        return "Pas d'image"

    image_apercu.short_description = 'Aperçu de l\'image'

admin.site.register(Product, ProductAdmin)
