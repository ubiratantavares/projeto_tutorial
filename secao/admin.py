from django.contrib import admin

from secao.models import Secao


class SecaoAdmin(admin.ModelAdmin):
    fields = ('nome', 'tutorial')
    list_display = ['nome', 'tutorial']
    search_fields = ['nome']
    list_filter = ['tutorial']


admin.site.register(Secao, SecaoAdmin)
