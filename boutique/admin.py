from django.contrib import admin
from .models import (
    Categorie,
    Produit,
    ImageProduit,
    Panier,
    ArticlePanier,
    Commande,
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
    list_display = ('utilisateur', 'date_creation', 'total')
    search_fields = ('utilisateur__username',)

    def total(self, obj):
        return obj.get_total()
    total.short_description = "Total du Panier"


@admin.register(ArticlePanier)
class ArticlePanierAdmin(admin.ModelAdmin):
    list_display = ('panier', 'produit', 'quantite', 'total_price')
    search_fields = ('produit__nom',)
    list_filter = ('panier__date_creation',)

    def total_price(self, obj):
        return obj.get_total_price()
    total_price.short_description = "Total Article"



@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'statut', 'total', 'date_commande')
    list_filter = ('statut', 'date_commande')
    search_fields = ('utilisateur__username',)
