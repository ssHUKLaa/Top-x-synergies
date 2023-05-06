# Generated by Django 4.1.7 on 2023-05-06 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topplayers', '0002_searchplayers_matches'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matches',
            name='player',
        ),
        migrations.RemoveField(
            model_name='matches',
            name='searchedPlayer',
        ),
        migrations.AddField(
            model_name='matches',
            name='Participants',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='searchplayers',
            name='match',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='topplayers.matches'),
        ),
    ]
