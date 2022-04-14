from django.db import models

from artigo.models import Artigo
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialArtigo(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    artigo = models.ForeignKey(Artigo, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'tutorial_artigo'
