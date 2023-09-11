from django.db import models
from article.models import Article
from author.models import Author

from django.utils.timezone import now


class ArticleAuthor(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'articleauthor'

