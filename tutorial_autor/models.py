from django.db import models

from autor.models import Autor
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialAutor(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    autor = models.ForeignKey(Autor, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'tutorial_autor'
