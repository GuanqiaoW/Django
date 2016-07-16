from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from dataInfo.models import Store,Staff,Sale,Product,Customer
from .forms import StoreForm,StaffForm,SaleForm,ProductForm,CustomerForm,LoginForm,UserForm,RegisterForm
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

# Purpose:add a new data
# Detail: create a new store with different args
# problem:  add duplicated data.
@login_required(login_url='/dataInfo/login/')
def addStore(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
		# create a form instance and populate it with data from the request:
        form = StoreForm(request.POST or None)
	# check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            if request.user.has_perm("add_store"):
            	form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/dataInfo/store_view/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = StoreForm()

    return render(request, 'dataInfo/add_store.html', {'form': form})

# # Purpose:update data with id
# # Detail: update data of new store
@login_required(login_url='/dataInfo/login/')
def updateStore(request,id=None):

	instance = get_object_or_404(Store,id=id)

	if request.POST:
		store_form = StoreForm(request.POST or None,instance = instance)
		if store_form.is_valid():
			store_form.save()
			return HttpResponseRedirect('/dataInfo/store_view/')
	else:
		store_form = StoreForm(instance = instance)

	return render_to_response('dataInfo/update_store.html', {'form': store_form,'id':instance.id}, context_instance=RequestContext(request))
# # Purpose:delete data with id
# # Detail: delete data of new store
# def deleteStore(request,id):
#
# 	if request.POST:
# 		Store.objects.filter(pk__in=id).delete()
#
# 	return HttpResponseRedirect('/dataInfo/store_view/')

# Purpose:view data
# Detail: view data of new store
# 1. get all store objects
# 2. display in the web page
@login_required(login_url='/dataInfo/login/')
def viewStore(request):
	if request.POST:

		if request.POST.get('delete_selected'):
			Store.objects.get(pk=request.POST.get('store_check')).delete()


		if request.POST.get('update_selected'):
			pk=request.POST.get('store_check')
			return HttpResponseRedirect(reverse('dataInfo:updateStore',kwargs={'id': pk}))

	view_store = Store.objects.all()
	context = {'view_store': view_store}
	return render(request, 'dataInfo/store_view.html', context)

def thanks(request):
	return HttpResponse("Thanks a lot")

# Purpose:create a staff profolio
# Detail: create a new store with different args
# add new staff object into user model and give permission of staff so that they can CRUD .
@login_required(login_url='/dataInfo/login/')
def createstaff(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
		# create a form instance and populate it with data from the request:
        form = StaffForm(request.POST or None)
	# check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # add to User model and give staff permission
            username = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            new_user = User.objects.create_user(username,email,password)
            new_user.is_active = True
            if request.POST.get('authorized'):
            	new_user.is_staff = True
            # redirect to a new URL:
            new_user.save()
            return HttpResponseRedirect('/dataInfo/staff_view/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = StaffForm()
    return render(request, 'dataInfo/create_staff.html', {'form': form})

# # Try to use ListView and show staff list
@login_required(login_url='/dataInfo/login/')
def staffview(request):
	if request.POST:

		if request.POST.get('delete_selected'):
			Staff.objects.get(pk=request.POST.get('staff_check')).delete()


		if request.POST.get('update_selected'):
			pk=request.POST.get('staff_check')
			return HttpResponseRedirect(reverse('dataInfo:updatestaff',kwargs={'id': pk}))
			
	view_staff = Staff.objects.all()
	context = {'view_staff': view_staff}
	return render(request, 'dataInfo/staff_list.html', context)

# #try to use DetailView and upadate infomation
@login_required(login_url='/dataInfo/login/')
def updatestaff(request,id=None):

	instance = get_object_or_404(Staff,id=id)
	if request.POST:
		staff_form = StaffForm(request.POST or None,instance=instance)
		if staff_form.is_valid():

			old_user = User.objects.get(username= request.POST.get('name'))
			print old_user.get_all_permissions()
			if request.POST.get('authorized')=='True':
				old_user.is_staff = True
			else:
				old_user.is_staff = False
			old_user.save()
			staff_form.save()
			return HttpResponseRedirect('/dataInfo/staff_view/')
	else:
		staff_form = StaffForm(instance=instance)
	return render_to_response('dataInfo/update_staff.html', {'form': staff_form,'id':instance.id}, context_instance=RequestContext(request))

# # try to use DeleteView and delete infomation
# def delete_staff(request):
@login_required(login_url='/dataInfo/login/')
def createsale(request):

    if request.method == 'POST':
        form = SaleForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dataInfo/sale_view/')
    else:
        form = SaleForm()
    return render(request, 'dataInfo/create_sale.html', {'form': form})

# def updatesale(request):

# def saleview(request):
@login_required(login_url='/dataInfo/login/')
def saleview(request):
	if request.POST:

		if request.POST.get('delete_selected'):
			Sale.objects.get(pk=request.POST.get('sale_check')).delete()

		if request.POST.get('update_selected'):
			pk=request.POST.get('sale_check')
			return HttpResponseRedirect(reverse('dataInfo:updatesale',kwargs={'id': pk}))
			
	view_sale = Sale.objects.all()
	context = {'view_sale': view_sale}
	return render(request, 'dataInfo/sale_list.html', context)

@login_required(login_url='/dataInfo/login/')
def updatesale(request,id=None):

	instance = get_object_or_404(Sale,id=id)
	if request.POST:
		sale_form = SaleForm(request.POST or None,instance=instance)
		if sale_form.is_valid():
			sale_form.save()
			return HttpResponseRedirect('/dataInfo/sale_view/')
	else:
		sale_form = SaleForm(instance=instance)
	return render_to_response('dataInfo/update_sale.html', {'form': sale_form,'id':instance.id}, context_instance=RequestContext(request))

# # try to use DeleteView and delete infomation
@login_required(login_url='/dataInfo/login/')
def createproduct(request):

    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dataInfo/product_view/')
    else:
        form = ProductForm()
    return render(request, 'dataInfo/create_product.html', {'form': form})

# def updatesale(request):

# def saleview(request):
@login_required(login_url='/dataInfo/login/')
def productview(request):
	if request.POST:

		if request.POST.get('delete_selected'):
			Product.objects.get(pk=request.POST.get('product_check')).delete()

		if request.POST.get('update_selected'):
			pk=request.POST.get('product_check')
			return HttpResponseRedirect(reverse('dataInfo:updateproduct',kwargs={'id': pk}))
			
	view_product = Product.objects.all()
	context = {'view_product': view_product}
	return render(request, 'dataInfo/product_list.html', context)

@login_required(login_url='/dataInfo/login/')
def updateproduct(request,id=None):

	instance = get_object_or_404(Product,id=id)
	
	if request.POST:
		product_form = ProductForm(request.POST or None,instance=instance)
		if product_form.is_valid():
			product_form.save()
			return HttpResponseRedirect('/dataInfo/product_view/')
	else:
		product_form = ProductForm(instance = instance)
	return render_to_response('dataInfo/update_product.html', {'form': product_form,'id':instance.id}, context_instance=RequestContext(request))

# THis method may be useless since A customer do not create other Customers.
@login_required(login_url='/dataInfo/login/')
def createcustomer(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dataInfo/customer_view/')
    else:
        form = CustomerForm()
    return render(request, 'dataInfo/create_customer.html', {'form': form})

@login_required(login_url='/dataInfo/login/')
def customerview(request):
	if request.POST:

		if request.POST.get('delete_selected'):
			Customer.objects.get(pk=request.POST.get('customer_check')).delete()

		if request.POST.get('update_selected'):
			pk=request.POST.get('customer_check')
			return HttpResponseRedirect(reverse('dataInfo:updatecustomer',kwargs={'id': pk}))
			
	view_customer = Customer.objects.all()
	context = {'view_customer': view_customer}
	return render(request, 'dataInfo/customer_list.html', context)

@login_required(login_url='/dataInfo/login/')
def updatecustomer(request,id=None):

	instance = get_object_or_404(Customer,id=id)
	
	if request.POST:
		customer_form = CustomerForm(request.POST or None,instance=instance)
		if customer_form.is_valid():
			customer_form.save()
			return HttpResponseRedirect('/dataInfo/customer_view/')
	else:
		customer_form = CustomerForm(instance = instance)
	return render_to_response('dataInfo/update_customer.html', {'form': customer_form,'id':instance.id}, context_instance=RequestContext(request))

# # try to use DeleteView and delete infomation


# login view: authroized user log in and then redirect to other view page
def login_view(request):
	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(name=username,password=password)
		if user is not None:
			# be activate in authenticate method
			if user.is_active:
				# login method:
				# If you have an authenticated user you want to attach to the current session 
				# this is done with a login() function.
				# Issue: problem in login()
				# Assumption 1: update_last_login
				# Assumption 2: 
				#
				login(request,user)
				#redirect to user profile
				print "suffcessful login!"

				# chech the user type 
				# if it is Customer,redirect to sale view
				# if it is Staff,redirect to userprofile
				if request.user.get_user_type() == "Customer":
					return HttpResponseRedirect('/dataInfo/sale_view')
				if request.user.get_user_type() == "Staff":
					# set permission to user
					request.user.asgin_perm("add_store")
					request.user.asgin_perm("add_product")
					request.user.asgin_perm("add_sale")
					request.user.asgin_perm("change_store")
					request.user.asgin_perm("change_product")
					request.user.asgin_perm("change_sale")
					request.user.asgin_perm("delete_store")
					request.user.asgin_perm("delete_product")
					request.user.asgin_perm("delete_sale")

					return HttpResponseRedirect('/dataInfo/userprofile')
			else:
				# return a disable account
				return HttpResponse("User acount or password is incorrect")
		else:
			# Return an 'invalid login' error message.
			print "Invalid login details: {0}, {1}".format(username, password)
			# redirect to login page
			return HttpResponseRedirect('/dataInfo/login')
	else:

		login_form = LoginForm()
	return render_to_response('dataInfo/login.html', {'form': login_form}, context_instance=RequestContext(request))

# logout view authroized user log in and then redirect to other view page
@login_required(login_url='/dataInfo/login/')
def logout_view(request):
	auth.logout(request)
	# rerdirect to login page
	return HttpResponseRedirect('/dataInfo/login')

@login_required(login_url='/dataInfo/login/')
def userprofile_view(request):
	print request.user.get_all_permissions()
	if request.method == 'POST':
		if request.POST.get('log_out'):
			return HttpResponseRedirect(reverse('dataInfo:logout_view'))
		# edit profile
		if request.POST.get('edit_profile'):
			#user edit form
			pk=request.POST.get('profile_check')
			return HttpResponseRedirect(reverse('dataInfo:updateprofile',kwargs={'id': pk}))
		if request.POST.get('store_view_direct'):
			return HttpResponseRedirect('/dataInfo/store_view')
		if request.POST.get('product_view_direct'):
			return HttpResponseRedirect('/dataInfo/product_view')
		if request.POST.get('sale_direct_direct'):
			return HttpResponseRedirect('/dataInfo/sale_view')
	else:
		pass
	view_user = User.objects.all()
	print view_user
	context = {'view_user': view_user}
	print context
	#problem in render
	return render(request, 'dataInfo/userprofile.html', context)


@login_required(login_url='/dataInfo/login/')
def updateprofile(request,id=None):
	instance = get_object_or_404(User,id=id)
	
	if request.POST:
		profile_form = UserForm(request.POST or None,instance=instance)
		if profile_form.is_valid():
			profile_form.save()
			return HttpResponseRedirect('/dataInfo/userprofile/')
	else:
		profile_form = UserForm(instance = instance)
	return render_to_response('dataInfo/editprofile.html', {'form': profile_form,'id':instance.id}, context_instance=RequestContext(request))



# sign in a new user and add user to different groups(staff or common user)
def register_view(request):
	print 'get herere'
	if request.method == 'POST':
		# save Customer or Staff in the model
		register_form = RegisterForm(request.POST or None)
		if register_form.is_valid():
			new_user = register_form.save()
			return HttpResponseRedirect('/dataInfo/userprofile')
	else:
		register_form = RegisterForm()
	return render(request, "dataInfo/register.html", {'form': register_form})




