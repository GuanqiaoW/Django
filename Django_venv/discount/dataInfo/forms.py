from django import forms
from .models import Store, Staff,Sale,Product,Customer
from django.forms.extras.widgets import SelectDateWidget
from datetime import date
from django.contrib.auth.models import User


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('store_name', 'street', 'district', 'city', 'province', 'longtitude', 'latitiude',)

class StaffForm(forms.ModelForm):

    store_id = forms.ModelChoiceField(queryset = Store.objects.all(),empty_label="--------") # select values ?
    class Meta:
        model = Staff
        fields = ('name','email','password','gender','birthday','is_staff','store_id')
        widgets = {'authorized':forms.RadioSelect,
                   'gender':forms.RadioSelect,
                    'birthday':SelectDateWidget(years=range(date.today().year-50,date.today().year))
        }
class SaleForm(forms.ModelForm):
 
    store_id = forms.ModelChoiceField(queryset = Store.objects.all(),empty_label="--------")
    product_id = forms.ModelChoiceField(queryset = Product.objects.all(),empty_label="--------") # select values ?

    class Meta:
        model = Sale
        fields = ('old_price','new_price','discount_start','discount_end','store_id','product_id')
        widgets = {
            'discount_start':SelectDateWidget,
            'discount_end':SelectDateWidget
        }
class ProductForm(forms.ModelForm):

    store_id = forms.ModelChoiceField(queryset = Store.objects.all(),empty_label="--------")
    
    class Meta:
        model = Product
        fields=('product_name','product_image','category','store_id')

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name','email','password','gender','birthday')
        widgets = {
                   'gender':forms.RadioSelect,
                    'birthday':SelectDateWidget(years=range(date.today().year-50,date.today().year))
        }

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields=('username','password')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('first_name','last_name','password')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('username','password','email')


# class RegisterCustomerForm

# class RegisterStaffForm
