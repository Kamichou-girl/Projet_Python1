from django.urls import path
from . import views

urlpatterns = [
    path('', views.boutique_home, name='boutique_home'),
    path('produit/<int:id>/', views.produit_detail, name='produit_detail'),
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/<int:id>/', views.categorie_detail, name='categorie_detail'),
    path('paniers/', views.paniers_list, name='paniers_list'),
    path('paniers/<int:id>/', views.panier_detail, name='panier_detail'),
    path('articles-panier/', views.articles_panier_list, name='articles_panier_list'),
    path('articles-panier/<int:id>/', views.article_panier_detail, name='article_panier_detail'),
    path('commandes/', views.commandes_list, name='commandes_list'),
    path('commandes/<int:id>/', views.commande_detail, name='commande_detail'),
    path('articles-commande/', views.articles_commande_list, name='articles_commande_list'),
    path('articles-commande/<int:id>/', views.article_commande_detail, name='article_commande_detail'),
    path('adresses/', views.adresses_livraison_list, name='adresses_livraison_list'),
    path('adresses/<int:id>/', views.adresse_livraison_detail, name='adresse_livraison_detail'),
] 