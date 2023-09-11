from django.contrib import admin

from tutorial.models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
    fields = ('name', 'link', 'last_updated', 'category')
    list_display = ['name', 'link', 'last_updated', 'category']
    search_fields = ['name']
    list_filter = ['category']


admin.site.register(Tutorial, TutorialAdmin)

