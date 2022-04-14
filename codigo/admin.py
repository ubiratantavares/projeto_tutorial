from django.contrib import admin

from codigo.models import Codigo


class CodigoAdmin(admin.ModelAdmin):
    fields = ('nome', 'implementado')
    list_display = ['nome', 'implementado']
    search_fields = ['nome']


admin.site.register(Codigo, CodigoAdmin)


