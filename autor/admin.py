from django.contrib import admin

from autor.models import Autor


class AutorAdmin(admin.ModelAdmin):
    fields = ('nome', )
    list_display = ['nome']
    search_fields = ['nome']


admin.site.register(Autor, AutorAdmin)
