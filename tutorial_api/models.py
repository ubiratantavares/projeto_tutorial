from django.db import models
from api.models import Api
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialApi(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    api = models.ForeignKey(Api, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'tutorial_api'
