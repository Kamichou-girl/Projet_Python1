from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

from .forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth import login

# === Pages principales ===
def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def single_product_view(request):
    return render(request, 'single-product.html')  

def single_blog_view(request):
    return render(request, 'single-blog.html')  

def cart_view(request):
    return render(request, 'cart.html')

def category_view(request):
    return render(request, 'category.html') 

def checkout_view(request):
    return render(request, 'checkout.html')

def tracking_view(request):
    return render(request, 'tracking.html')

def elements_view(request):
    return render(request, 'elements.html')

def contact_process(request):
    return render(request, 'contact.html') 



def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')    


# === Vue de connexion ===
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
                return redirect('index')  # Redirige vers la page d'accueil
            else:
                messages.error(request, "Identifiants invalides ❌")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                # Envoi de l'email de confirmation
                send_mail(
                    subject='Bienvenue chez Accessoires Dhabi! 🎉',
                    message=f"""Bonjour {user.username},

Nous vous remercions de votre inscription sur Accessoires Dhabi!
Votre compte a été créé avec succès.

À très bientôt sur notre site!

Cordialement,
L'équipe Accessoires Dhabi""",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email],
                    fail_silently=False,
                )
                # Connexion automatique
                login(request, user)
                messages.success(request, "Inscription réussie! Un email de confirmation vous a été envoyé. ✅")
                return redirect('index')
            except Exception as e:
                print(f"Erreur d'envoi d'email: {e}")
                messages.error(request, "Inscription réussie mais erreur lors de l'envoi de l'email de confirmation.")
                return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form}) 

    