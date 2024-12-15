from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contactinfo
from .forms import ContactForm, CatagoryForm, ProductForm, ProductImagesForm
from products.models import Category, Products, ProductImages


# admin apis
class adminlogin(View):
    def get(self, request):
        return render(request, "admin.html")
    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Log in the user
            login(request, user)
            return redirect("admindashboard")
        else:
            messages.error(request, "Invalid username or password.")
        return render(request, 'admin.html')


class AdminLogout(View):
    def get(self, request):
        logout(request)
        return redirect("adminlogin")


class admindashboard(LoginRequiredMixin,View):
    login_url = 'adminlogin'
    def get(self, request):
        contact = Contactinfo.objects.all().last()
        return render(request, "admindash.html",{"contact":contact})
    
    def post(self, request):
        contact = Contactinfo.objects.all().first()
        if contact:
            form = ContactForm(request.POST, instance=contact)
            if form.is_valid():
                form.save()
                messages.success(request, "Contact info updated successfully!")
                return redirect("admindashboard")
            else:
                messages.error(request, "Invalied fields")
                return redirect("admindashboard")

        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Contact info updated successfully!")
                return redirect("admindashboard")
            else:
                messages.error(request, "Invalied fields")
                return redirect("admindashboard")
            

class Catagories(LoginRequiredMixin,View):
    def get(self, request):
        catagory = Category.objects.all()
        return render(request, "catagory.html", {"catagory": catagory})


class SubmitCatagory(LoginRequiredMixin,View):
    def post(self, request):
        data = request.POST
        files = request.FILES
        print("files :", files)
        form = CatagoryForm(data, files)
        if form.is_valid():
            pln_obj = form.save()
        else:
            print(form.errors)
        return redirect("admincatagory")


class DeleteCatagory(LoginRequiredMixin,View):
    def post(self, request):
        id = request.POST.get("catagory_id")
        cat = Category.objects.get(id=id)
        if cat:
            cat.delete()
        return redirect("admincatagory")
    


class ProductView(LoginRequiredMixin,View):
    def get(self, request):
        products = Products.objects.all()
        catagory  = Category.objects.all()
        return render(request, "products.html", {"products":products, "catagory":catagory})
    
    def post(self, request):
        data = request.POST
        files = request.FILES
        form = ProductForm(data)
        print(files)
        if form.is_valid():
            pln_obj = form.save()
            ProductImages.objects.create(product=pln_obj, image=files.get("image"))
        return redirect("products")
    

class DeleteProduct(LoginRequiredMixin,View):
    def post(self, request):
        id = request.POST.get("product_id")
        product = Products.objects.get(id=id)
        if product:
            product.delete()
        return redirect("products")