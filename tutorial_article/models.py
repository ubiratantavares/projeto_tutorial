from django.db import models
from tutorial.models import Tutorial
from article.models import Article
from django.utils.timezone import now


class TutorialArticle(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'tutorialarticle'
