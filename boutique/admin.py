from django.contrib import admin
from .models import (
    Categorie,
    Produit,
    ImageProduit,
    Panier,
    ArticlePanier,
    Commande,
    ArticleCommande,
    AdresseLivraison,
)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)


class ImageProduitInline(admin.TabularInline):
    model = ImageProduit
    extra = 1


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'prix', 'stock', 'date_ajout')
    list_filter = ('categorie',)
    search_fields = ('nom', 'description')
    inlines = [ImageProduitInline]


@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'date_creation')
    search_fields = ('utilisateur__username',)


@admin.register(ArticlePanier)
class ArticlePanierAdmin(admin.ModelAdmin):
    list_display = ('panier', 'produit', 'quantite')
    search_fields = ('produit__nom',)
    list_filter = ('panier__date_creation',)


class ArticleCommandeInline(admin.TabularInline):
    model = ArticleCommande
    extra = 1


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'statut', 'total', 'date_commande')
    list_filter = ('statut', 'date_commande')
    search_fields = ('utilisateur__username',)
    inlines = [ArticleCommandeInline]


@admin.register(ArticleCommande)
class ArticleCommandeAdmin(admin.ModelAdmin):
    list_display = ('commande', 'produit', 'quantite', 'prix_unitaire')
    search_fields = ('produit__nom',)


@admin.register(AdresseLivraison)
class AdresseLivraisonAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'ville', 'pays', 'code_postal')
    search_fields = ('utilisateur__username', 'ville', 'pays')
