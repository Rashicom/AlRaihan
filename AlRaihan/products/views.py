from django.shortcuts import render
from django.views import View
from .models import Category, Products, ProductImages

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class Shop(View):
    def get(self, request):
        return render(request, 'shop.html')
    
class AboutUs(View):
    def get(self, request):
        return render(request, 'about.html')
    

class Services(View):
    def get(self, request):
        return render(request, 'services.html')
    

class blog(View):
    def get(self, request):
        return render(request, 'blog.html')


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
