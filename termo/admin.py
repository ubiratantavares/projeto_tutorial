from django.contrib import admin

from termo.models import Termo


class TermoAdmin(admin.ModelAdmin):
    fields = ('nome', 'descricao')
    list_display = ['nome', 'descricao']
    search_fields = ['nome']


admin.site.register(Termo, TermoAdmin)

