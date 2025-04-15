from django.contrib import admin
from .models import Article, Categorie, Commentaire

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'date_publication']

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom']

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ['article', 'utilisateur', 'date']
