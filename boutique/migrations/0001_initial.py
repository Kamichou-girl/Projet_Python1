# Generated by Django 5.2 on 2025-04-13 19:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdresseLivraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=255)),
                ('ville', models.CharField(max_length=100)),
                ('code_postal', models.CharField(max_length=20)),
                ('pays', models.CharField(max_length=100)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(choices=[('en_attente', 'En attente'), ('expediee', 'Expédiée'), ('livree', 'Livrée')], default='en_attente', max_length=20)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='produits/')),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='boutique.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='ImageProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='produits/')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='boutique.produit')),
            ],
        ),
        migrations.CreateModel(
            name='ArticlePanier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(default=1)),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='boutique.panier')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boutique.produit')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('prix_unitaire', models.DecimalField(decimal_places=2, max_digits=8)),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='boutique.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boutique.produit')),
            ],
        ),
    ]
