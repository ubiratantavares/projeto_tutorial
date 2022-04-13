from django.contrib import admin

from tipo.models import Tipo


class TipoAdmin(admin.ModelAdmin):
    fields = ('nome', )
    list_display = ['nome']
    search_fields = ['nome']


admin.site.register(Tipo, TipoAdmin)
