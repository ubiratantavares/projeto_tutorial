from django.db import models

from termo.models import Termo
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialTermo(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    termo = models.ForeignKey(Termo, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'tutorial_termo'
