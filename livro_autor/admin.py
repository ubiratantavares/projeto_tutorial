from django.contrib import admin

from livro_autor.models import LivroAutor


class LivroAutorAdmin(admin.ModelAdmin):
    fields = ('livro', 'autor', 'data_criacao')
    list_display = ['livro', 'autor', 'data_criacao']
    list_filter = ['livro', 'autor']


admin.site.register(LivroAutor, LivroAutorAdmin)
