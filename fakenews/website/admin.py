from django.contrib import admin

from .models import Statement

class AdminStatement(admin.ModelAdmin):
	list_display = ['title','description']
admin.site.register(Statement, AdminStatement)