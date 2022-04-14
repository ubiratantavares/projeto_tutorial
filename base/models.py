from django.db import models


class Base(models.Model):
    nome = models.CharField(max_length=250, db_index=True)
    link_base = models.CharField(max_length=250, blank=True)
    link_descricao = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'base'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
