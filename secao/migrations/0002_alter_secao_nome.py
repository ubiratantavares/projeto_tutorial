# Generated by Django 4.0.2 on 2022-04-14 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secao',
            name='nome',
            field=models.CharField(db_index=True, max_length=150),
        ),
    ]
