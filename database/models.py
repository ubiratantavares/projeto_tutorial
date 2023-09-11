from django.db import models


class DataBase(models.Model):
    filename = models.CharField(max_length=250, db_index=True)
    link_data = models.CharField(max_length=250, blank=True)
    link_names = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'database'
        ordering = ('filename',)

    def __str__(self):
        return self.filename
