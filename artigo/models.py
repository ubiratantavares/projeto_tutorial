from django.db import models


class Artigo(models.Model):
    nome = models.CharField(max_length=150, db_index=True)
    link = models.CharField(max_length=250, blank=True)
    ano = models.IntegerField(default=1900)

    class Meta:
        db_table = 'artigo'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
