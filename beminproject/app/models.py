from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

    def __str__(self):
        return self.name