from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Categorie, Produit, ImageProduit, Panier, ArticlePanier, Commande

# Serializer pour l'utilisateur
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        ref_name = 'BoutiqueUserSerializer'

# Serializer pour les catégories
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom', 'description']
        ref_name = 'BoutiqueCategorieSerializer'

# Serializer pour les images de produit
class ImageProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProduit
        fields = ['id', 'produit', 'image']
        ref_name = 'BoutiqueImageProduitSerializer'

# Serializer pour les produits
class ProduitSerializer(serializers.ModelSerializer):
    categorie = CategorieSerializer(read_only=True)
    images = ImageProduitSerializer(many=True, read_only=True)

    class Meta:
        model = Produit
        fields = [
            'id', 'nom', 'description', 'prix', 'stock', 'image', 
            'categorie', 'images', 'date_ajout'
        ]
        ref_name = 'BoutiqueProduitSerializer'

# Serializer pour les articles du panier
class ArticlePanierSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer(read_only=True)
    panier = serializers.PrimaryKeyRelatedField(queryset=Panier.objects.all())

    class Meta:
        model = ArticlePanier
        fields = ['id', 'panier', 'produit', 'quantite', 'get_total_price']
        ref_name = 'BoutiqueArticlePanierSerializer'

# Serializer pour les paniers
class PanierSerializer(serializers.ModelSerializer):
    utilisateur = UserSerializer(read_only=True)
    articles = ArticlePanierSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Panier
        fields = ['id', 'utilisateur', 'articles', 'date_creation', 'total']
        ref_name = 'BoutiquePanierSerializer'

    def get_total(self, obj):
        return obj.get_total()

# Serializer pour les commandes
class CommandeSerializer(serializers.ModelSerializer):
    utilisateur = UserSerializer(read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Commande
        fields = [
            'id', 'utilisateur', 'statut', 'total', 'date_commande'
        ]
        ref_name = 'BoutiqueCommandeSerializer'