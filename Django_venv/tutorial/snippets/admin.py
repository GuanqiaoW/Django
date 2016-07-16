from django.contrib import admin
from .models import Snippet

class SnippetAdmin(admin.ModelAdmin):

	list_display =["created","title","code","linenos","language","style"]
	list_display_links =["created","title","code","linenos","language","style"]
	class Meta:
		model= Snippet

admin.site.register(Snippet,SnippetAdmin)
