from django.contrib import admin

from database.models import DataBase


class DataBaseAdmin(admin.ModelAdmin):
    fields = ('filename', 'link_data', 'link_names')
    list_display = ['filename', 'link_data', 'link_names']
    search_fields = ['filename']


admin.site.register(DataBase, DataBaseAdmin)
