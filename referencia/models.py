from django.db import models
from tipo.models import Tipo


class Referencia(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=250, db_index=True)
    autor = models.CharField(max_length=100, blank=True)
    link = models.CharField(max_length=250, blank=True)
    ano = models.IntegerField(blank=True)

    class Meta:
        db_table = 'referencia'

    def __str__(self):
        return self.nome
