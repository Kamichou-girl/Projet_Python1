from django.shortcuts import render, get_object_or_404, redirect
from .models import Categorie, Article, Commentaire
from .forms import CommentaireForm
from django.contrib import messages

def blog_home(request):
    posts = Post.objects.filter(est_publie=True).order_by('-date_publication')
    return render(request, 'blog/home.html', {'posts': posts})

def categorie_detail(request, slug):
    categorie = get_object_or_404(Categorie, slug=slug)
    posts = categorie.posts.filter(est_publie=True).order_by('-date_publication')
    return render(request, 'blog/categorie_detail.html', {'categorie': categorie, 'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, est_publie=True)
    commentaires = post.commentaires.filter(est_approuve=True).order_by('date_creation')

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.post = post
            # Si l'utilisateur est authentifié, on remplit le champ auteur
            if request.user.is_authenticated:
                commentaire.auteur = request.user
            commentaire.est_approuve = True  # Vous pouvez modifier la logique d'approbation
            commentaire.save()
            messages.success(request, "Votre commentaire a été ajouté.")
            return redirect('post_detail', slug=slug)
    else:
        form = CommentaireForm()

    context = {
        'post': post,
        'commentaires': commentaires,
        'form': form,
    }
    return render(request, 'blog/post_detail.html', context)
