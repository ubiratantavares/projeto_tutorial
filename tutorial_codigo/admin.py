from django.contrib import admin

from tutorial_codigo.models import TutorialCodigo


class TutorialCodigoAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'codigo', 'data_criacao')
    list_display = ['tutorial', 'codigo', 'data_criacao']
    list_filter = ['tutorial', 'codigo']


admin.site.register(TutorialCodigo, TutorialCodigoAdmin)