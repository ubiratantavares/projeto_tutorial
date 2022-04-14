from django.db import models


class Problema(models.Model):
    nome = models.CharField(max_length=50, db_index=True, unique=True)

    class Meta:
        db_table = 'problema'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
