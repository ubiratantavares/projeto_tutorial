from django.contrib import admin

from tutorial_artigo.models import TutorialArtigo


class TutorialArtigoAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'artigo', 'data_criacao')
    list_display = ['tutorial', 'artigo', 'data_criacao']
    list_filter = ['tutorial', 'artigo']


admin.site.register(TutorialArtigo, TutorialArtigoAdmin)
