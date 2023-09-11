# Generated by Django 4.0.2 on 2023-01-06 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('link', models.CharField(max_length=250, unique=True)),
                ('year', models.IntegerField(default=1990)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tutoriais', to='category.category')),
            ],
            options={
                'db_table': 'tutorial',
                'ordering': ('name',),
            },
        ),
    ]
