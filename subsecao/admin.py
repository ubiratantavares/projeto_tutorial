from django.contrib import admin

from subsecao.models import Subsecao


class SubsecaoAdmin(admin.ModelAdmin):
    fields = ('secao', 'nome')
    list_display = ['secao', 'nome']
    search_fields = ['nome']
    list_filter = ['secao']


admin.site.register(Subsecao, SubsecaoAdmin)
