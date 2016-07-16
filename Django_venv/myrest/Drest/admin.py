from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
  fields = ['firstname', 'lastname','pub_date']

admin.site.register(Person, PersonAdmin)
# Register your models here.
