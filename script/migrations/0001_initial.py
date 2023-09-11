# Generated by Django 4.0.2 on 2023-01-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(db_index=True, max_length=50)),
                ('package', models.CharField(blank=True, max_length=50)),
                ('implemented', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'script',
                'ordering': ('filename',),
            },
        ),
    ]
