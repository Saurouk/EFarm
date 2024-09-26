from rest_framework import viewsets, generics
from .models import Product
from .serializers import ProductSerializer

# Product ViewSet pour lister et afficher les détails des produits
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ProductCreateView pour créer un nouveau produit
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
