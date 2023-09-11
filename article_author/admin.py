from django.contrib import admin

from article_author.models import ArticleAuthor


class ArticleAuthorAdmin(admin.ModelAdmin):
    fields = ('article', 'author')
    list_display = ['article', 'author']
    list_filter = ['article', 'author']


admin.site.register(ArticleAuthor, ArticleAuthorAdmin)
