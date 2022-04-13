from django.contrib import admin

from tutorial.models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
    fields = ('topico', 'referencias', 'termos', 'problemas', 'nome', 'script', 'link', 'cod_disponivel',
              'cod_implementado')
    list_display = ['nome', 'link', 'script', 'cod_disponivel', 'cod_implementado']
    search_fields = ['nome']
    list_filter = ['topico', 'referencias', 'termos', 'problemas']


admin.site.register(Tutorial, TutorialAdmin)
