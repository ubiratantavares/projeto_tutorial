from django.db import models


class Termo(models.Model):
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    sigla = models.CharField(max_length=20, db_index=True, unique=True)

    class Meta:
        db_table = 'termo'

    def __str__(self):
        return self.nome
