from django.db import models

from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialTutorial(models.Model):
    origin = models.ForeignKey(Tutorial, related_name="referenceds", on_delete=models.DO_NOTHING)
    referenced = models.ForeignKey(Tutorial, related_name="origins",  on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now)


    class Meta:
        db_table = 'tutorialtutorial'
