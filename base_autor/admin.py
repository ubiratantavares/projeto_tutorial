from django.contrib import admin

from base_autor.models import BaseAutor


class BaseAutorAdmin(admin.ModelAdmin):
    fields = ('base', 'autor', 'data_criacao')
    list_display = ['base', 'autor', 'data_criacao']
    list_filter = ['base', 'autor']


admin.site.register(BaseAutor, BaseAutorAdmin)
