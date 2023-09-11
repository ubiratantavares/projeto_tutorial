from django.contrib import admin

from tutorial_author.models import TutorialAuthor


class TutorialAuthorAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'author')
    list_display = ['tutorial', 'author']
    list_filter = ['tutorial', 'author']


admin.site.register(TutorialAuthor, TutorialAuthorAdmin)
