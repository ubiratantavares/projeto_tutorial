from django.db import models


class Script(models.Model):
    filename = models.CharField(max_length=50, db_index=True)
    package = models.CharField(max_length=50, blank=True)
    implemented = models.BooleanField(default=False)

    class Meta:
        db_table = 'script'
        ordering = ('filename',)

    def __str__(self):
        return "{} - {}".format(self.package, self.filename)
