from django.contrib import admin

from livro.models import Livro


class LivroAdmin(admin.ModelAdmin):
    fields = ('nome', 'link', 'ano')
    list_display = ['nome', 'link', 'ano']
    search_fields = ['nome']


admin.site.register(Livro, LivroAdmin)
