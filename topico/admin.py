from django.contrib import admin
from topico.models import Topico


class TopicoAdmin(admin.ModelAdmin):
    fields = ('nome', )
    list_display = ['nome']
    search_fields = ['nome']


admin.site.register(Topico, TopicoAdmin)
