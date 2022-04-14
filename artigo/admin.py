from django.contrib import admin

from artigo.models import Artigo


class ArtigoAdmin(admin.ModelAdmin):
    fields = ('nome', 'link', 'ano')
    list_display = ['nome', 'link', 'ano']
    search_fields = ['nome']


admin.site.register(Artigo, ArtigoAdmin)

