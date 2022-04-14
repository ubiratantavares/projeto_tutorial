from django.contrib import admin

from tutorial_livro.models import TutorialLivro


class TutorialLivroAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'livro', 'data_criacao')
    list_display = ['tutorial', 'livro', 'data_criacao']
    list_filter = ['tutorial', 'livro']


admin.site.register(TutorialLivro, TutorialLivroAdmin)
