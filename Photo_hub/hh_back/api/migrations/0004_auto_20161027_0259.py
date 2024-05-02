# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-26 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161015_1212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['-creationDate']},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['-creationDate']},
        ),
        migrations.RenameField(
            model_name='album',
            old_name='creation_date',
            new_name='creationDate',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='creation_date',
            new_name='creationDate',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='album',
            name='name',
        ),
        migrations.AddField(
            model_name='album',
            name='title',
            field=models.CharField(default='New album', max_length=80),
        ),
    ]
