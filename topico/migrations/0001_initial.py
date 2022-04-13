# Generated by Django 4.0.2 on 2022-04-12 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=50, unique=True)),
            ],
            options={
                'db_table': 'topico',
                'ordering': ('nome',),
            },
        ),
    ]
