# Generated by Django 3.1.4 on 2021-01-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201231_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='timeout_puzzles',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='solved_puzzles',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]