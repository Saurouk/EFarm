from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

from product.models import Product
from product.serializers import ProductSerializer


# Product ViewSet pour lister et afficher les détails des produits
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@method_decorator(login_required(login_url='/admin/login/'), name='dispatch')
# ProductCreateView pour créer un nouveau produit
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]  # Restreint l'accès aux utilisateurs admin

