from django.shortcuts import render
from django.views import View
from .models import Category, Products, ProductImages
import random


class HomeView(View):
    def get(self, request):
        catagories = Category.objects.all()
        random_pks = random.sample([row.pk for row in catagories],3)
        random_catagories = catagories.filter(pk__in=random_pks)
        return render(request, 'index.html', {"catagories": catagories, "random_catagories":random_catagories,"heading":"Explore the products"})


class Shop(View):
    def get(self, request):
        products = Products.objects.all()
        catagories = Category.objects.all()
        return render(request, 'shop.html', {"Products":products,"catagories":catagories,"heading":"Explore the products"})


class Categories(View):
    def get(self, request, category_id):
        all_catagories = Category.objects.all()
        category = all_catagories.filter(pk=category_id).last()
        products = Products.objects.filter(category=category)
        return render(request, 'shop.html', {"Products":products,"catagories":all_catagories,"heading":category.name})


class Contact(View):
    def get(self, request):
        catagories = Category.objects.all()
        return render(request, 'contact.html',{"catagories":catagories})
    
class Cart(View):
    def get(self, request):
        return render(request, 'cart.html')
    

class Checkout(View):
    def get(self, request):
        catagories = Category.objects.all()
        return render(request, 'checkout.html',{"catagories":catagories})
    
class Thank(View):
    def get(self, request):
        catagories = Category.objects.all()
        return render(request, 'thankyou.html',{"catagories":catagories})


