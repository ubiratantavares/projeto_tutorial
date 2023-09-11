from django.contrib import admin

from tutorial_book.models import TutorialBook


class TutorialBookAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'book', 'cited')
    list_display = ['tutorial', 'book', 'cited']
    list_filter = ['tutorial', 'book', 'cited']


admin.site.register(TutorialBook, TutorialBookAdmin)
