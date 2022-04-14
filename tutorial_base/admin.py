from django.contrib import admin

from tutorial_base.models import TutorialBase


class TutorialBaseAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'base', 'data_criacao')
    list_display = ['tutorial', 'base', 'data_criacao']
    list_filter = ['tutorial', 'base']


admin.site.register(TutorialBase, TutorialBaseAdmin)
