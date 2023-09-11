from django.contrib import admin

from tutorial_wikipedia.models import TutorialWikipedia


class TutorialWikipediaAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'wikipedia')
    list_display = ['tutorial', 'wikipedia']
    list_filter = ['tutorial', 'wikipedia']


admin.site.register(TutorialWikipedia, TutorialWikipediaAdmin)
