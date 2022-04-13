from django.contrib import admin

from secao.models import Secao


class SecaoAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'nome')
    list_display = ['tutorial', 'nome']
    search_fields = ['nome']
    list_filter = ['tutorial']


admin.site.register(Secao, SecaoAdmin)
