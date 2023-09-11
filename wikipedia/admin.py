from django.contrib import admin

from wikipedia.models import Wikipedia


class WikipediaAdmin(admin.ModelAdmin):
    fields = ('name', 'link')
    list_display = ['name', 'link']
    search_fields = ['name']


admin.site.register(Wikipedia, WikipediaAdmin)
