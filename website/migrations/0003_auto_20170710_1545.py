# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20170710_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]