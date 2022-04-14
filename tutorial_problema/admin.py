from django.contrib import admin

from tutorial_problema.models import TutorialProblema


class TutorialProblemaAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'problema', 'data_criacao')
    list_display = ['tutorial', 'problema', 'data_criacao']
    list_filter = ['tutorial', 'problema']


admin.site.register(TutorialProblema, TutorialProblemaAdmin)
