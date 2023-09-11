from django.db import models

from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    year = models.IntegerField(default=1990)

    class Meta:
        db_table = 'book'
        ordering = ('name',)

    def __str__(self):
        return self.name

