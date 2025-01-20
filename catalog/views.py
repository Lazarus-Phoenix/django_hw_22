from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def product_list(request):
    products = Product.objects.all()
    context={ 'products' : products }
    return render(request, "product_list.html", context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def index(request):
    return render(request,"base.html")