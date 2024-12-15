from django.forms import ModelForm
from .models import Contactinfo
from products.models import Category, Products, ProductImages 

class ContactForm(ModelForm):
    class Meta:
        model = Contactinfo
        fields = "__all__"

class CatagoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

class ProductImagesForm(ModelForm):
    class Meta:
        model = ProductImages
        fields = "__all__"