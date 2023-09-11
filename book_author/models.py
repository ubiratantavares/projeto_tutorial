from django.db import models
from author.models import Author
from book.models import Book

from django.utils.timezone import now


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'bookautor'
