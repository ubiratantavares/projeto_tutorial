from django.contrib import admin

from tutorial_database.models import TutorialDataBase


class TutorialDataBaseAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'database')
    list_display = ['tutorial', 'database']
    list_filter = ['tutorial', 'database']


admin.site.register(TutorialDataBase, TutorialDataBaseAdmin)
