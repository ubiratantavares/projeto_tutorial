from django.db import models

from script.models import Script
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialScript(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    script = models.ForeignKey(Script, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'tutorialscript'
