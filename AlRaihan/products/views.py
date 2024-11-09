from django.shortcuts import render
from django.views import View
from .models import Category, Products, ProductImages


class HomeView(View):
    def get(self, request):
        catagories = Category.objects.all()[:3]
        for i in catagories:
            print(i.image.url)
        return render(request, 'index.html', {"catagories": catagories})


class Shop(View):
    def get(self, request):
        products = Products.objects.all()
        return render(request, 'shop.html', {"Products":products})


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')
    
class Cart(View):
    def get(self, request):
        return render(request, 'cart.html')
    

class Checkout(View):
    def get(self, request):
        return render(request, 'checkout.html')
    
class Thank(View):
    def get(self, request):
        return render(request, 'thankyou.html')
