from django.db import models
from topico.models import Topico
from problema.models import Problema
from referencia.models import Referencia
from termo.models import Termo
from problema.models import Problema


class Tutorial(models.Model):
    topico = models.ForeignKey(Topico, related_name='tutoriais', on_delete=models.DO_NOTHING)
    referencias = models.ManyToManyField(Referencia)
    termos = models.ManyToManyField(Termo)
    problemas = models.ManyToManyField(Problema)
    nome = models.CharField(max_length=250, db_index=True, unique=True)
    link = models.CharField(max_length=250, db_index=True, unique=True)
    script = models.CharField(max_length=50, db_index=True, default="nome do script python")
    cod_disponivel = models.BooleanField(default=False)
    cod_implementado = models.BooleanField(default=False)


    class Meta:
        db_table = 'tutorial'

    def __str__(self):
        return self.nome
