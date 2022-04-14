from django.db import models

from problema.models import Problema
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialProblema(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    problema = models.ForeignKey(Problema, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'tutorial_problema'
