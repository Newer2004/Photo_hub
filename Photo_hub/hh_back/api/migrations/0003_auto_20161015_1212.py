# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-15 09:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20161015_0657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='owner',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='owner',
            new_name='user',
        ),
    ]