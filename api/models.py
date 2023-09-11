from django.db import models


class API(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    link = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'api'
        ordering = ('name',)

    def __str__(self):
        return self.name
