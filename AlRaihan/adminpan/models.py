from django.db import models

# Create your models here.
class Contactinfo(models.Model):
    address = models.TextField()
    mobile_number = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    
