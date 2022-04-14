from django.db import models

from tutorial.models import Tutorial

from django.utils.timezone import now


class TutorialTutorial(models.Model):
    tutorial_origem = models.ForeignKey(Tutorial, related_name="tutoriais_refs", on_delete=models.DO_NOTHING)
    tutorial_referencia = models.ForeignKey(Tutorial, related_name="tutoriais_origens",  on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(default=now)


    class Meta:
        db_table = 'tutorial_tutorial'
