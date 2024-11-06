from django.contrib import admin
from .models import Category, Products, ProductImages

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'description', 'specification', 'price', 'discount', 'is_in_offer')

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
