from django.contrib import admin

from problema.models import Problema


class ProblemaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


admin.site.register(Problema, ProblemaAdmin)



