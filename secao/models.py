from django.db import models
from tutorial.models import Tutorial


class Secao(models.Model):
    tutorial = models.ForeignKey(Tutorial, related_name='secoes', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100, db_index=True, unique=True)

    class Meta:
        db_table = 'secao'

    def __str__(self):
        return self.nome
