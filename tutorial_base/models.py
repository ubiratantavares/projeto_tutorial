from django.db import models

from base.models import Base
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialBase(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    base = models.ForeignKey(Base, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'tutorial_base'
