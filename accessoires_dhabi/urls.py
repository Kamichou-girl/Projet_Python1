from django.contrib import admin
from django.urls import path, include
from accessoires_dhabi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart_view, name='cart'),
    path('category/', views.category_view, name='category'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('single-product/', views.single_product_view, name='single-product'),
    path('single-blog/', views.single_blog_view, name='single-blog'),
    path('tracking/', views.tracking_view, name='tracking'),
    path('elements/', views.elements_view, name='elements'),
    path('contact/process/', views.contact_process, name='contact_process'),
    path('boutique/', include('boutique.urls')),  # ✅ Inclusion correcte ici SEULEMENT
]
