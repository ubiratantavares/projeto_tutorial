from django.db import models

from autor.models import Autor
from base.models import Base

from django.utils.timezone import now


class BaseAutor(models.Model):
    base = models.ForeignKey(Base, related_name="baseautor1", on_delete=models.DO_NOTHING)
    autor = models.ForeignKey(Autor, related_name="baseautor2", on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'base_autor'
