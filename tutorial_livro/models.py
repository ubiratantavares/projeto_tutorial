from django.db import models

from livro.models import Livro
from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialLivro(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.DO_NOTHING)
    livro = models.ForeignKey(Livro, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'tutorial_livro'
