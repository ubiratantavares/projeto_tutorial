from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=50, db_index=True)

    class Meta:
        db_table = 'autor'
        ordering = ('nome',)
        

    def __str__(self):
        return self.nome

