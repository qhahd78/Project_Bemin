from django.db import models

# Create your models here.!

class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    store = models.CharField(max_length=20)
    menu = models.CharField(max_length=50)
    side = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Store(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=20)
    intro = models.TextField()
    
    def __str__(self):
        return self.name