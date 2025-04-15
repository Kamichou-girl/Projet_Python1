from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='produits/', blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class ImageProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='produits/')

    def __str__(self):
        return f"Image pour {self.produit.nom}"


class Panier(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Panier de {self.utilisateur.username}"

    def get_total(self):
        """
        Calcule le total du panier en sommant le total de chaque article.
        """
        return sum(item.get_total_price() for item in self.articles.all())


class ArticlePanier(models.Model):
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE, related_name='articles')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"

    def get_total_price(self):
        """
        Retourne le total (prix x quantité) pour cet article.
        """
        return self.produit.prix * self.quantite


class Commande(models.Model):
    STATUT_CHOIX = [
        ('en_attente', 'En attente'),
        ('expediee', 'Expédiée'),
        ('livree', 'Livrée'),
    ]

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commandes')
    statut = models.CharField(max_length=20, choices=STATUT_CHOIX, default='en_attente')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande #{self.id} - {self.utilisateur.username}"

    def update_total(self):
        """
        Met à jour le total de la commande en se basant sur ses articles.
        """
        self.total = sum(article.get_total_price() for article in self.articles.all())
        self.save()


    def produit_detail(request, id):
           produit = Produit.objects.get(id=id)
           return render(request, 'boutique/produit_detail.html', {'produit': produit})