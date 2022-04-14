from django.contrib import admin

from artigo_autor.models import ArtigoAutor


class ArtigoAutorAdmin(admin.ModelAdmin):
    fields = ('artigo', 'autor', 'data_criacao')
    list_display = ['artigo', 'autor', 'data_criacao']
    list_filter = ['autor', 'artigo']


admin.site.register(ArtigoAutor, ArtigoAutorAdmin)
