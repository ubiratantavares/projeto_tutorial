from django.db import models
from secao.models import Secao


class Subsecao(models.Model):
    secao = models.ForeignKey(Secao, related_name='subsecoes', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100, db_index=True, unique=True)

    class Meta:
        db_table = 'subsecao'

    def __str__(self):
        return self.nome
