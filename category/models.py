from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)

    class Meta:
        db_table = 'category'
        ordering = ('name',)

    def __str__(self):
        return self.name

