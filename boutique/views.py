from django.shortcuts import render
from boutique.models import Produit, Categorie , Panier, ArticlePanier 
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Assure-toi que c’est bien l'app `boutique`

def boutique_home(request):
    return render(request, 'boutique/index.html')


def produit_detail(request, id):
    produit = get_object_or_404(Produit, id=id)
    context = {'produit': produit}
    return render(request, 'single-blog.html', context)

def categories_list(request):
    return render(request, 'boutique/categories.html')

def categorie_detail(request, id):
    return render(request, 'boutique/categorie_detail.html', {'id': id})

@login_required
def paniers_list(request):
    try:
        # On suppose que chaque utilisateur a un unique panier actif
        panier = Panier.objects.get(utilisateur=request.user)
    except Panier.DoesNotExist:
        panier = None  # Ou vous pouvez créer un nouveau panier ici

    context = {
        'panier': panier,
    }
    return render(request, 'cart.html', context)
def panier_detail(request, id):
    return render(request, 'boutique/panier_detail.html', {'id': id})

def articles_panier_list(request):
    return render(request, 'boutique/articles_panier.html')

def article_panier_detail(request, id):
    return render(request, 'boutique/article_panier_detail.html', {'id': id})

def commandes_list(request):
    return render(request, 'boutique/commandes.html')

def commande_detail(request, id):
    return render(request, 'boutique/commande_detail.html', {'id': id})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                
                login(request, user)
                messages.success(request, "Connexion réussie ✅")
                return redirect('home')  # à adapter selon ta page d’accueil
    else:
        form = LoginForm()
    return render(request, 'Login.html', {'form': form})    
 

def category_view(request):
    # Récupère toutes les catégories pour la barre latérale
    categories = Categorie.objects.all()
    
    # Récupère le paramètre ?category= dans l'URL pour filtrer les produits
    category_id = request.GET.get('category')
    if category_id:
        category = get_object_or_404(Categorie, id=category_id)
        produits = Produit.objects.filter(categorie=category)
    else:
        category = None  # Aucune catégorie sélectionnée
        produits = Produit.objects.all()
    
    context = {
        'categories': categories,
        'produits': produits,
        'category': category,   # Pour afficher le titre ou la description de la catégorie sélectionnée
    }
    return render(request, 'category.html', context)

def produit_detail(request, id):
    produit = get_object_or_404(Produit, id=id)
    context = {
        'produit': produit
    }
    return render(request, 'produit_detail.html', context)    

def categorie_detail(request, id):
    # Récupère la catégorie sélectionnée
    category = get_object_or_404(Categorie, id=id)
    # Récupère tous les produits associés à cette catégorie
    produits = Produit.objects.filter(categorie=category)
    # Pour la barre latérale, on souhaite afficher toutes les catégories
    categories = Categorie.objects.all()
    
    context = {
        'category': category,   # Catégorie actuelle
        'produits': produits,   # Produits filtrés par catégorie
        'categories': categories,  # Liste de toutes les catégories pour le menu latéral
    }
    return render(request, 'category.html', context)


@login_required
def ajouter_au_panier(request, produit_id):
    if request.method == 'POST':
        produit = get_object_or_404(Produit, id=produit_id)
        try:
            quantity = int(request.POST.get('qty', 1))
        except ValueError:
            quantity = 1

        # Récupération ou création du panier de l'utilisateur
        panier, created = Panier.objects.get_or_create(utilisateur=request.user)
        
        # Récupération ou création de l'article dans le panier
        article, created = ArticlePanier.objects.get_or_create(
            panier=panier,
            produit=produit,
            defaults={'quantite': quantity}
        )
        if not created:
            article.quantite += quantity
            article.save()

        # Redirection vers la page du panier
        return redirect('boutique:paniers_list')
    return redirect('boutique:produit_detail', id=produit_id)

@login_required
def checkout_view(request):
    # Récupère (ou crée) le panier actif de l'utilisateur.
    panier, created = Panier.objects.get_or_create(utilisateur=request.user, is_active=True)
    context = {'panier': panier}
    return render(request, 'checkout.html', context)

# Vue checkout_success : simule le traitement du paiement, affiche un message de succès et redirige vers la page des catégories.
@login_required
def checkout_success(request):
    # Vous pouvez, par exemple, marquer le panier comme inactif ici.
    messages.success(request, "Votre paiement a été effectué avec succès!")
    return redirect('boutique:categories_list')

