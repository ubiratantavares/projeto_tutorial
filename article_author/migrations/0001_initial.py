# Generated by Django 4.0.2 on 2023-01-06 19:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='article.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='author.author')),
            ],
            options={
                'db_table': 'articleauthor',
            },
        ),
    ]
