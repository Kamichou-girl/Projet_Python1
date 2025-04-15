from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .viewsets import UserViewSet,PostViewSet, CategorieViewSet, ArticleViewSet, CommentaireViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAuthenticated


app_name = 'blog'

# Configuration de l'API avec DRF
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'posts', PostViewSet)
router.register(r'commentaires', CommentaireViewSet)

# Vue pour générer la documentation Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Blog",
        default_version='v1',
        description="Documentation de l'API de gestion de blog",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@blog.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=False,
    permission_classes=(IsAuthenticated,),
)

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('categorie/<slug:slug>/', views.categorie_detail, name='categorie_detail'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),

    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
