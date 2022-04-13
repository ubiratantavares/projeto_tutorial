from django.contrib import admin

from referencia.models import Referencia


class ReferenciaAdmin(admin.ModelAdmin):
    fields = ('tipo', 'nome', 'autor', 'link', 'ano')
    list_display = ['tipo', 'nome', 'autor', 'link', 'ano']
    search_fields = ['nome']
    list_filter = ['tipo']


admin.site.register(Referencia, ReferenciaAdmin)
