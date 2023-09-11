from django.db import models

from book.models import Book
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialBook(models.Model):
    cited = models.CharField(max_length=50, blank=True)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'tutorialbook'
