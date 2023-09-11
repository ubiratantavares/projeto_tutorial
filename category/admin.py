from django.contrib import admin
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
