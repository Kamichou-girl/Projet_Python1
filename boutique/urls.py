from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .viewsets import (
    UserViewSet, CategorieViewSet, ProduitViewSet, ImageProduitViewSet,
    PanierViewSet, ArticlePanierViewSet, CommandeViewSet
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAuthenticated

app_name = 'boutique'

# Configuration de l'API avec DRF
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'produits', ProduitViewSet)
router.register(r'images-produit', ImageProduitViewSet)
router.register(r'paniers', PanierViewSet)
router.register(r'articles-panier', ArticlePanierViewSet)
router.register(r'commandes', CommandeViewSet)

# Vue pour générer la documentation Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Boutique",
        default_version='v1',
        description="Documentation de l'API de gestion de la boutique",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@boutique.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=False,
    permission_classes=(IsAuthenticated,),
)


urlpatterns = [
    # Accueil de la boutique
    path('', views.boutique_home, name='boutique_home'),

    # Détails du produit
    path('produit/<int:id>/', views.produit_detail, name='produit_detail'),

    # Liste et détails des catégories
    path('categories/', views.category_view, name='categories_list'),
    path('categories/<int:id>/', views.categorie_detail, name='categorie_detail'),
    path('ajouter-au-panier/<int:produit_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    # Paniers et détail d'un panier
    path('paniers/', views.paniers_list, name='paniers_list'),
    path('paniers/<int:id>/', views.panier_detail, name='panier_detail'),

    # Articles du panier
    path('articles-panier/', views.articles_panier_list, name='articles_panier_list'),
    path('articles-panier/<int:id>/', views.article_panier_detail, name='article_panier_detail'),
    path('produit/<int:id>/', views.produit_detail, name='produit_detail'),
    path('cart/', views.paniers_list, name='paniers_list'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),

    path('login/', views.login_view, name='login_view'),

    # Commandes et détails d'une commande
    path('commandes/', views.commandes_list, name='commandes_list'),
    path('commandes/<int:id>/', views.commande_detail, name='commande_detail'),

    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
