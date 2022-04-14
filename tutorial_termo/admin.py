from django.contrib import admin

from tutorial_termo.models import TutorialTermo


class TutorialTermoAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'termo', 'data_criacao')
    list_display = ['tutorial', 'termo', 'data_criacao']
    list_filter = ['tutorial', 'termo']


admin.site.register(TutorialTermo, TutorialTermoAdmin)
