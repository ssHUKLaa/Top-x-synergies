# Generated by Django 4.1.7 on 2023-06-06 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topplayers', '0002_searchplayers_tier'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='set_number',
            field=models.IntegerField(default=0),
        ),
    ]