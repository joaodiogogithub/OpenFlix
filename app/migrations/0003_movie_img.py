# Generated by Django 5.1.1 on 2024-10-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_movie_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
