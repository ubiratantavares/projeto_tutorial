# Generated by Django 4.0.2 on 2022-04-14 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigo_autor', '0002_alter_artigoautor_data_criacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artigoautor',
            options={},
        ),
        migrations.RemoveField(
            model_name='artigoautor',
            name='nome',
        ),
    ]
