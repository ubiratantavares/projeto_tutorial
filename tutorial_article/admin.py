from django.contrib import admin

from tutorial_article.models import TutorialArticle


class TutorialArticleAdmin(admin.ModelAdmin):
    fields = ('tutorial', 'article')
    list_display = ['tutorial', 'article']
    list_filter = ['tutorial', 'article']


admin.site.register(TutorialArticle, TutorialArticleAdmin)
