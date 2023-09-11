from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    link = models.CharField(max_length=250, blank=True)
    year = models.IntegerField(default=1990)

    class Meta:
        db_table = 'article'
        ordering = ('name',)

    def __str__(self):
        return self.name
