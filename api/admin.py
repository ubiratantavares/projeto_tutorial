from django.contrib import admin

from api.models import API


class APIAdmin(admin.ModelAdmin):
    fields = ('name', 'link')
    list_display = ['name', 'link']
    search_fields = ['name']


admin.site.register(API, APIAdmin)
