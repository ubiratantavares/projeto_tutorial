from django.contrib import admin

from author.models import Author


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Author, AuthorAdmin)
