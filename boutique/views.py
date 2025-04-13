from django.shortcuts import render

def boutique_home(request):
    return render(request, 'boutique/index.html')

def produit_detail(request, id):
    return render(request, 'boutique/produit_detail.html', {'id': id})

def categories_list(request):
    return render(request, 'boutique/categories.html')

def categorie_detail(request, id):
    return render(request, 'boutique/categorie_detail.html', {'id': id})

def paniers_list(request):
    return render(request, 'boutique/paniers.html')

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

def articles_commande_list(request):
    return render(request, 'boutique/articles_commande.html')

def article_commande_detail(request, id):
    return render(request, 'boutique/article_commande_detail.html', {'id': id})

def adresses_livraison_list(request):
    return render(request, 'boutique/adresses_livraison.html')

def adresse_livraison_detail(request, id):
    return render(request, 'boutique/adresse_livraison_detail.html', {'id': id})
