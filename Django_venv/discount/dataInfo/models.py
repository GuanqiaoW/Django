from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Store(models.Model):
  
  # products = models.ForeignKey(Products)  # one to many relationship, one store can have many products
  store_name = models.TextField()
  street = models.CharField(max_length=100)
  district = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  province = models.CharField(max_length=100)
  longtitude = models.DecimalField(max_digits=999,decimal_places=6)
  latitiude = models.DecimalField(max_digits=999,decimal_places=6)
  created = models.DateTimeField(default= datetime.now, blank=True)
  
  def __str__(self):
    return self.store_name


class Product(models.Model):
  
  
  product_name = models.CharField(max_length=100)
  product_image =  models.CharField(max_length=100)
  category = models.CharField(max_length=100,blank = True)
  published_time = models.DateTimeField(default = datetime.now,blank = False,null=False)
  store_id = models.ForeignKey(Store,default=1)   # store_id to reference with stores
  
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

  def __str__(self):
  
    return self.product_name

class Customer(models.Model):

  yes_or_no = ((True, 'Yes'),(False, 'No'))
  male_or_female = ((True,'Male'),(False,'Female'))
  
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100,blank = False, null = False)
  password = models.CharField(max_length=100)
  gender = models.BooleanField(default = True, choices = male_or_female)
  birthday = models.DateField(default =None,blank = False, null = False)
  created = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.name

class Staff(models.Model):

  yes_or_no = ((True, 'Yes'),(False, 'No'))
  male_or_female = ((True,'Male'),(False,'Female'))

  name = models.CharField(max_length=100,blank = False, null = False)
  email = models.EmailField(max_length=100,blank = False, null = False)
  password = models.CharField(max_length=100,blank = False, null = False)
  gender = models.BooleanField(default = True, choices = male_or_female)
  birthday = models.DateField(default =None,blank = False, null = False)
  created = models.DateTimeField(default=datetime.now, blank=True)
  authorized = models.BooleanField(default=False,choices = yes_or_no) 
  store_id = models.ForeignKey(Store,default=1) # relate ModelChoiceField in ModelFrom

  def __str__(self):
    return self.name

class Sale(models.Model):

  old_price = models.DecimalField(max_digits=1000,decimal_places=2,blank=False,null=False)
  new_price = models.DecimalField(max_digits=1000,decimal_places=2,blank=False,null=False)
  discount_start = models.DateField(blank = False,null=False)
  discount_end = models.DateField(blank = False,null=False)
  created = models.DateTimeField(default=datetime.now, blank=True)
  store_id = models.ForeignKey(Store,default=1)   # store_id to reference with stores
  product_id = models.ForeignKey(Product,default=1) # product_id to reference with different products


  # --Probelm--: cause problem to display value in DecimalField in django admin
  # --solution--: convert integer value to string by formation
  def __str__(self):
    return "%.2f" %self.new_price
