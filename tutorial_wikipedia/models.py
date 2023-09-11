from django.db import models

from tutorial.models import Tutorial
from wikipedia.models import Wikipedia

from django.utils.timezone import now


class TutorialWikipedia(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    wikipedia = models.ForeignKey(Wikipedia, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'tutorialwikipedia'
