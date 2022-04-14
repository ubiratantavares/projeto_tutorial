from django.db import models

from topico.models import Topico


class Tutorial(models.Model):
    topico = models.ForeignKey(Topico, related_name='tutoriais', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=250, db_index=True)
    link = models.CharField(max_length=250, db_index=True, unique=True)

    class Meta:
        db_table = 'tutorial'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

