# Generated by Django 3.0 on 2019-12-05 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0002_auto_20191205_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='metateam',
            name='health',
            field=models.IntegerField(default=24),
        ),
    ]