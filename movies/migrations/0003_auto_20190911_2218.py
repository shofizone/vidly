# Generated by Django 2.2 on 2019-09-11 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
