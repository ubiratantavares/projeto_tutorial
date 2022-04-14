from django.db import models


class Codigo(models.Model):
    nome = models.CharField(max_length=50, db_index=True)
    implementado = models.BooleanField(default=False)

    class Meta:
        db_table = 'codigo'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
