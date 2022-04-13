# Generated by Django 4.0.2 on 2022-04-12 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problema', '0001_initial'),
        ('referencia', '0001_initial'),
        ('termo', '0001_initial'),
        ('topico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=250, unique=True)),
                ('link', models.CharField(db_index=True, max_length=250, unique=True)),
                ('cod_disponivel', models.BooleanField(default=False)),
                ('cod_implementado', models.BooleanField(default=False)),
                ('problemas', models.ManyToManyField(to='problema.Problema')),
                ('referencias', models.ManyToManyField(to='referencia.Referencia')),
                ('termos', models.ManyToManyField(to='termo.Termo')),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tutoriais', to='topico.topico')),
            ],
            options={
                'db_table': 'tutorial',
            },
        ),
    ]
