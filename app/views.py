from django.shortcuts import render
from .models import Gallery,Product

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html',{'products':products})

def gallery(request):
    image=Gallery.objects.all()
    return render(request, 'gallery.html', {'image': image})

def contact(request):
    return render(request, 'contact.html')


    
