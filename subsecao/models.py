from django.db import models

from secao.models import Secao


class Subsecao(models.Model):
    secao = models.ForeignKey(Secao, related_name='subsecoes', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=50, db_index=True)


    class Meta:
        db_table = 'subsecao'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
