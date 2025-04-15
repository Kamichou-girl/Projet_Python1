from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from .models import Categorie, Produit, ImageProduit, Panier, ArticlePanier, Commande
from .serializers import (
    UserSerializer, CategorieSerializer, ProduitSerializer, ImageProduitSerializer,
    PanierSerializer, ArticlePanierSerializer, CommandeSerializer
)

# ViewSet pour les utilisateurs
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ViewSet pour les catégories
class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ViewSet pour les produits
class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ViewSet pour les images de produit
class ImageProduitViewSet(viewsets.ModelViewSet):
    queryset = ImageProduit.objects.all()
    serializer_class = ImageProduitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ViewSet pour les paniers
class PanierViewSet(viewsets.ModelViewSet):
    queryset = Panier.objects.all()
    serializer_class = PanierSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ViewSet pour les articles du panier
class ArticlePanierViewSet(viewsets.ModelViewSet):
    queryset = ArticlePanier.objects.all()
    serializer_class = ArticlePanierSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ViewSet pour les commandes
class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]