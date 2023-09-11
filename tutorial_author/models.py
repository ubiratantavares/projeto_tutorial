from django.db import models

from author.models import Author
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialAuthor(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'tutorialauthor'

    def __str__(self):
        return self.tutorial.name


