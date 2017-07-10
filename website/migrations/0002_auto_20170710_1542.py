# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('subject', models.CharField(max_length=100)),
                ('qualification', models.CharField(choices=[('owl', 'Owl'), ('newt', 'Newt'), ('above newt', 'Above Newt')], max_length=30)),
                ('experience', models.IntegerField(default=0)),
                ('research_areas', models.CharField(max_length=500)),
                ('picture', models.FileField(upload_to=b'')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
    ]
