from django.db import models
from artigo.models import Artigo
from autor.models import Autor

from django.utils.timezone import now

class ArtigoAutor(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.DO_NOTHING)
    autor = models.ForeignKey(Autor, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'artigo_autor'

