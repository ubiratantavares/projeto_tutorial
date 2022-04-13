from django.db import models

from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=50, db_index=True, unique=True)

    class Meta:
        db_table = 'tipo'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

