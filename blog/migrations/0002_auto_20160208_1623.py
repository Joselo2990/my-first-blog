# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 22:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tilte',
            new_name='title',
        ),
    ]
