from django.contrib import admin

from tutorial_script.models import TutorialScript


class TutorialScriptAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'script')
    list_display = ['tutorial', 'script']
    list_filter = ['tutorial', 'script']


admin.site.register(TutorialScript, TutorialScriptAdmin)
