from django.db import models

from codigo.models import Codigo
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialCodigo(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    codigo = models.ForeignKey(Codigo, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'tutorial_codigo'
