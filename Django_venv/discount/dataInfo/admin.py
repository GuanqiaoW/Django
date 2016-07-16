from django.contrib import admin
from .models import Product,Store,Customer,Staff,Sale
# Register your models here.
from django.contrib.auth.models import Permission

class ProductAdmin(admin.ModelAdmin):

	list_display = ["pk","product_name","product_image","category","store_id","published_time"]
	list_display_links = ["pk","product_name","product_image","category","store_id",
	"published_time"]
	class Meta:
		model = Product

	#display foreign key's attribute in the table
	def store_id(self,instance):
		return instance.store_id.id

class StoreAdmin(admin.ModelAdmin):

	list_display =["pk","store_name","street","city","province","longtitude","latitiude","created"]
	list_display_links =["pk","store_name","street","city","province","longtitude","latitiude","created"]
	class Meta:
		model= Store

#--Problem--: list_editable can not display primary id 
#--Solution--: 
class CustomerAdmin(admin.ModelAdmin):

	list_display = ["pk","name","email","password","gender","birthday","is_active","last_login","created"]
	list_display_links = ["pk","name","email","password","gender","birthday","is_active","last_login","created"]
	class Meta:
		model = Customer

class SaleAdmin(admin.ModelAdmin):

	list_display = ["pk","product_id","old_price","new_price","discount_start","discount_end","store_id","created"]
	list_display_links = ["pk","product_id","old_price","new_price","discount_start","discount_end","store_id","created"]
	class Meta:
		model = Sale
	#--display foreign key's attribute in the table--
	def store_id(self, instance):
		return instance.store_id.id
	# def old_price(self,instance):
	# 	return "%.2f" %instance.old_price
	# def new_price(self,instance):
	# 	return "%.2f" %instance.new_price
	def product_id(self, instance):
		return instance.product_id.name

class StaffAdmin(admin.ModelAdmin):
	list_display = ["pk","name","email","password","gender","birthday","is_staff","store_id","is_active","last_login","created"]
	list_display_links = ["pk","name","email","password","gender","birthday","is_staff","store_id","is_active","last_login","created"]
	class Meta:
		model = Staff

	#--display foreign key's attribute in the table--
	def store_id(self, instance):
		return instance.store_id.id

admin.site.register(Permission)
admin.site.register(Sale,SaleAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Staff,StaffAdmin)