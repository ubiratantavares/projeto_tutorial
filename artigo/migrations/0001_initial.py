# Generated by Django 4.0.2 on 2022-04-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=150)),
                ('link', models.CharField(blank=True, max_length=250)),
                ('ano', models.IntegerField(default=1900)),
            ],
            options={
                'db_table': 'artigo',
                'ordering': ('nome',),
            },
        ),
    ]
