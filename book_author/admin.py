from django.contrib import admin

from book_author.models import BookAuthor


class BookAuthorAdmin(admin.ModelAdmin):
    fields = ('book', 'author')
    list_display = ['book', 'author']
    list_filter = ['book', 'author']


admin.site.register(BookAuthor, BookAuthorAdmin)
