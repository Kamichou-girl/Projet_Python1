from django.shortcuts import render

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