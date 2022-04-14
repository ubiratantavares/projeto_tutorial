from django.db import models
from autor.models import Autor
from livro.models import Livro

from django.utils.timezone import now


class LivroAutor(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.DO_NOTHING)
    autor = models.ForeignKey(Autor, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'livro_autor'