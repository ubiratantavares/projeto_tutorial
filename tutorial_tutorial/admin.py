from django.contrib import admin

from tutorial_tutorial.models import TutorialTutorial


class TutorialTutorialAdmin(admin.ModelAdmin):
    fields = ('tutorial_origem', 'tutorial_referencia', 'data_criacao')
    list_display = ['tutorial_origem', 'tutorial_referencia', 'data_criacao']
    list_filter = ['tutorial_origem', 'tutorial_referencia']


admin.site.register(TutorialTutorial, TutorialTutorialAdmin)
