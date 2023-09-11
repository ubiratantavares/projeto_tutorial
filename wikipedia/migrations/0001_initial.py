# Generated by Django 4.0.2 on 2023-01-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wikipedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('link', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'db_table': 'wikipedia',
                'ordering': ('name',),
            },
        ),
    ]