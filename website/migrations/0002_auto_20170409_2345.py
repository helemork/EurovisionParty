# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='dress',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='plagiarism',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
    ]
