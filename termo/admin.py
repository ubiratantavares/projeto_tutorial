from django.contrib import admin

from termo.models import Termo


class TermoAdmin(admin.ModelAdmin):
    fields = ('nome', 'sigla')
    list_display = ['nome', 'sigla']
    search_fields = ['nome']


admin.site.register(Termo, TermoAdmin)
