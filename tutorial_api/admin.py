from django.contrib import admin

from tutorial_api.models import TutorialApi


class TutorialApiAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'api', 'data_criacao')
    list_display = ['tutorial', 'api', 'data_criacao']
    list_filter = ['tutorial', 'api']


admin.site.register(TutorialApi, TutorialApiAdmin)

