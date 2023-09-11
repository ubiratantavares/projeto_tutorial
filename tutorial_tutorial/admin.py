from django.contrib import admin

from tutorial_tutorial.models import TutorialTutorial


class TutorialTutorialAdmin(admin.ModelAdmin):
    fields = ('origin', 'referenced')
    list_display = ['origin', 'referenced']
    list_filter = ['origin', 'referenced']


admin.site.register(TutorialTutorial, TutorialTutorialAdmin)
