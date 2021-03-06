# Generated by Django 4.0.2 on 2022-04-14 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('secao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsecao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=50)),
                ('secao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subsecoes', to='secao.secao')),
            ],
            options={
                'db_table': 'subsecao',
                'ordering': ('nome',),
            },
        ),
    ]
