# Generated by Django 3.1.5 on 2021-01-26 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20210125_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='num_players_solved',
        ),
        migrations.AddField(
            model_name='question',
            name='num_solves',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of users that solved this question'),
        ),
    ]
