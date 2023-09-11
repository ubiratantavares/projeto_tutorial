from django.contrib import admin

from article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    fields = ('name', 'link', 'year')
    list_display = ['name', 'link', 'year']
    search_fields = ['name']


admin.site.register(Article, ArticleAdmin)

