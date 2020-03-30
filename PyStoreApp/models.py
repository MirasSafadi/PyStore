from django.db import models

# Create your models here.
class Product(models.Model):
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
  
    def __str__(self):
        return str(self.name) + ' | ' + str(self.description) + ' | ' + str(self.price)

class User(models.Model):
    privilege = models.CharField(max_length=20,default=0)
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
        
    def __str__(self):
        return str(self.full_name) + ' | ' + str(self.email) + ' | ' + str(self.mobile)