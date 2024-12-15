from django.db import models
from PIL import Image
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="catagory")
    def __str__(self):
        return str(f"Category: {self.name}")
    
class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    specification = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.IntegerField(default=0)
    is_in_offer = models.BooleanField(default=False)

    def __str__(self):
        return str(f"Product: {self.name}")

    @property
    def get_first_image(self):
        # Retrieve the first image associated with this product, if it exists
        first_image = self.productimages_set.first()
        if first_image:
            return first_image.image.url if first_image.image else None
        return None
class ProductImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = ResizedImageField(size=[477, 477],crop=['middle', 'center'],upload_to='product_images/')

    def __str__(self):
        return str(f"Image for Product: {self.product.name}")