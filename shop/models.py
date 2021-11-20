# changes over here are directly reflected in the database
# i shall migrate after making any kind of changes to the model(obj)

from django.db import models
from django.utils import timezone

# Create your models here.

# model is nothing but objects of a class
# these obj contain all the required attributes
class Product(models.Model):

    # defining instance variables 
    # all the fields/attribs required for the obj
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    category = models.CharField(max_length=50,default='')
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    # full uploading path : /media/shop/images
    image = models.ImageField(upload_to='shop/images',default='')

    # to display name of the product(obj)
    # this method is overrided from parent class
    def __str__(self):
        return self.product_name

class Feedback(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    # date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    itemsJSON = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    order_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()

    def __str__(self):
        return self.firstname

class OrderUpdate(models.Model):
    # Agenda : Push multiple updates(desc) for same order_id 
    # & then display them matching the Order.order_id entered by the customer
    # in order of the timestamps
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=1000)
    timestamp = models.DateField(auto_now_add=True)
    update_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.update_desc[0:30]+""