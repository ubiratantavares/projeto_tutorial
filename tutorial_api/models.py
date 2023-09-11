from django.db import models
from api.models import API
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialAPI(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    api = models.ForeignKey(API, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'tutorialapi'
