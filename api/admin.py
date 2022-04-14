from django.contrib import admin

from api.models import Api


class ApiAdmin(admin.ModelAdmin):
    fields = ('nome', 'link')
    list_display = ['nome', 'link']
    search_fields = ['nome']


admin.site.register(Api, ApiAdmin)
