from django.contrib import admin

from book.models import Book


class BookAdmin(admin.ModelAdmin):
    fields = ('name', 'year')
    list_display = ['name', 'year']
    search_fields = ['name']


admin.site.register(Book, BookAdmin)
