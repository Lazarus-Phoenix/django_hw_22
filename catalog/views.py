from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


def product_detail(reqest, pk):

    return render(reqest, "product_detail")

def index(request):
    return render(request,"base.html")