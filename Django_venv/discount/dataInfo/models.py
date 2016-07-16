from __future__ import unicode_literals
from django.contrib.auth.models import Permission
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractBaseUser

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
  # _store_id_r = models.IntegerField(default=1)

  # @property
  # def store_id_r(self):
  #   return self._store_id_r
  # @store_id_r.setter
  # def store_id_r(self,value):
  #   self._store_id_r = value

  
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
  _is_active = models.BooleanField(default = False,db_column="is_active")
  last_login = models.DateTimeField(default = timezone.now,auto_now=True, auto_now_add=False,db_column="last_login")
  # a single unique field that can be used for identification 

  @property
  def is_active(self):
    return self._is_active
  @is_active.setter
  def is_active(self,value):
    self._is_active = value

  def is_authenticated(self):
    return True

  def get_user_type(self):
    return "Customer"

  def has_perm(self,perm,object=None):
    return 

  def __str__(self):
    return self.name
# inherit from User
# user method in user
class Staff(AbstractBaseUser):

  yes_or_no = ((True, 'Yes'),(False, 'No'))
  male_or_female = ((True,'Male'),(False,'Female'))

  name = models.CharField(max_length=100,blank = False, null = False)
  email = models.EmailField(max_length=100,blank = False, null = False)
  gender = models.BooleanField(default = True, choices = male_or_female)
  birthday = models.DateField(default =None,blank = False, null = False)
  created = models.DateTimeField(default=datetime.now, blank=True)
  is_staff = models.BooleanField(default=False,choices = yes_or_no) 
  store_id = models.ForeignKey(Store,default=1) # relate ModelChoiceField in ModelFrom
  # store_id_r = models.IntegerField(default=1)
  # a single unique field that can be used for identification 

  # add cosutomer permission for staff 
  REQUIRED_FIELDS = ['email']
  class Meta:
        permissions = (
            ("can_drive", "Can drive"),
        )
  
  perm_list = set()
  def get_user_type(self):
    return "Staff"

  def has_perm(self, perm, obj=None):
    if perm in self.get_all_permissions():
      return True
    return False
  
  def get_all_permissions(self, obj=None):
        return self.perm_list

  def asgin_perm(self,perm,object=None):
    self.perm_list.add(perm)
  
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
  # store_id_r = models.IntegerField(default=1)
  # product_id_r = models.IntegerField(default=1)

  # @property
  # def store_id_r(self):
  #   return self._store_id_r
  # @store_id_r.setter
  # def store_id_r(self,value):
  #   self._store_id_r = value

  # @property
  # def product_id_r(self):
  #   return self._product_id_r
  # @product_id_r.setter
  # def product_id_r(self,value):
  #   self._product_id_r = value

  # --Probelm--: cause problem to display value in DecimalField in django admin
  # --solution--: convert integer value to string by formation
  def __str__(self):
    return "%.2f" %self.new_price
