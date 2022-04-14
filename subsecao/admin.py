from django.contrib import admin

from subsecao.models import Subsecao


class SubsecaoAdmin(admin.ModelAdmin):
    fields = ('nome', 'secao')
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['secao']


admin.site.register(Subsecao, SubsecaoAdmin)
