from django.db import models

# Create your models here.

class Product(models.Model):
    
    name = models.TextField(max_length=50, verbose_name="name")
    description = models.TextField(max_length=200, verbose_name="description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")
    available = models.BooleanField(default=True, verbose_name="available")
    photo = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="photo")
    
    def __str__(self):
        return self.name
