from django.db import models

from database.models import DataBase
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialDataBase(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    database = models.ForeignKey(DataBase, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now)


    class Meta:
        db_table = 'tutorialdatabase'
