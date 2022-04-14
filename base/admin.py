from django.contrib import admin

from base.models import Base


class BaseAdmin(admin.ModelAdmin):
    fields = ('nome', 'link_base', 'link_descricao')
    list_display = ['nome', 'link_base', 'link_descricao']
    search_fields = ['nome']


admin.site.register(Base, BaseAdmin)
