from django.db import models


class Termo(models.Model):
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    descricao = models.CharField(max_length=100, db_index=True)

    class Meta:
        db_table = 'termo'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
