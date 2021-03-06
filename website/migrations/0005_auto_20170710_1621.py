# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20170710_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='faculty',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Subject'),
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(to='website.Subject'),
        ),
    ]
