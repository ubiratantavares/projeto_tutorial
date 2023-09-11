from django.contrib import admin

from tutorial_api.models import TutorialAPI


class TutorialAPIAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'api')
    list_display = ['tutorial', 'api']
    list_filter = ['tutorial', 'api']


admin.site.register(TutorialAPI, TutorialAPIAdmin)

