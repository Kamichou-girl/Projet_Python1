from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accessoires_dhabi import views
from django.urls import path
from django.contrib.auth.models import User
from .views import login_view
from .views import register_view
from boutique.views import category_view as boutique_views_category  # Correction ici
from rest_framework import routers, serializers, viewsets 



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart_view, name='cart'),
    path('category/', boutique_views_category, name='category'),  # Correction ici
    path('checkout/', views.checkout_view, name='checkout'),
    path('single-product/', views.single_product_view, name='single-product'),
    path('single-blog/', views.single_blog_view, name='single-blog'),
    path('tracking/', views.tracking_view, name='tracking'),
    path('elements/', views.elements_view, name='elements'),
    path('contact/process/', views.contact_process, name='contact_process'),
    path('boutique/', include('boutique.urls')),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('blog/', include('blog.urls')),
    path('boutique/', include('boutique.urls')),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('blog/', include('blog.urls')),

    

    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
