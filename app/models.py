from django.db import models

# Create your models here.

class Gallery(models.Model):
    image= models.ImageField(upload_to='gallery_images/')

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
