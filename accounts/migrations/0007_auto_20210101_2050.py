# Generated by Django 3.1.4 on 2021-01-01 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210101_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='solved_puzzles',
            new_name='solved_questions',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='timeout_puzzles',
            new_name='timeout_questions',
        ),
    ]