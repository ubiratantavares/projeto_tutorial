from django.contrib import admin

from script.models import Script


class ScriptAdmin(admin.ModelAdmin):
    fields = ('filename', 'package', 'implemented')
    list_display = ['filename', 'package', 'implemented']
    search_fields = ['filename']


admin.site.register(Script, ScriptAdmin)


