from django.db import models

from category.models import Category
from django.utils.timezone import now


class Tutorial(models.Model):
    category = models.ForeignKey(Category, related_name='tutoriais', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=250, db_index=True, unique=True)
    link = models.CharField(max_length=250, unique=True)
    last_updated = models.DateField(default=now)

    class Meta:
        db_table = 'tutorial'
        ordering = ('name',)

    def __str__(self):
        return self.name

