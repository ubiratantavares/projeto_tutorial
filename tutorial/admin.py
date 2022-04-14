from django.contrib import admin

from tutorial.models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
    fields = ('nome', 'link', 'topico')
    list_display = ['nome', 'link', 'topico']
    search_fields = ['nome']
    list_filter = ['topico']


admin.site.register(Tutorial, TutorialAdmin)

