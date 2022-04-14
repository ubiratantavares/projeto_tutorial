from django.contrib import admin

from tutorial_autor.models import TutorialAutor


class TutorialAutorAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'autor', 'data_criacao')
    list_display = ['tutorial', 'autor', 'data_criacao']
    list_filter = ['tutorial', 'autor']


admin.site.register(TutorialAutor, TutorialAutorAdmin)
