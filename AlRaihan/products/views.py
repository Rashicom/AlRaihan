from django.shortcuts import render
from django.views import View
from .models import Category, Products, ProductImages

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
