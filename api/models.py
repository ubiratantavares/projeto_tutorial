from django.db import models


class Api(models.Model):
    nome = models.CharField(max_length=150, db_index=True)
    link = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'api'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
