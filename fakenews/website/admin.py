from django.contrib import admin

from .models import Statement
from .models import Article

class AdminStatement(admin.ModelAdmin):
	list_display = ['id','title','fakeness']
admin.site.register(Statement, AdminStatement)

class AdminArticle(admin.ModelAdmin):
    def get_name(self, obj):
    	return obj.statement.title
    get_name.admin_order_field  = 'title'  #Allows column order sorting
    get_name.short_description = 'Title'  #Renames column head
    list_display = ['id','title','statement','get_name']

admin.site.register(Article, AdminArticle)