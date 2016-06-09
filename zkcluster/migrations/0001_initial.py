# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 12:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('serialnumber', models.CharField(max_length=100, unique=True)),
                ('ip', models.CharField(max_length=15, unique=True)),
                ('port', models.IntegerField(default=4370)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=28)),
                ('privilege', models.SmallIntegerField(choices=[(0, 'User'), (14, 'Administrator')], default=0)),
                ('password', models.CharField(blank=True, max_length=8, null=True)),
                ('group_id', models.CharField(blank=True, max_length=7, null=True)),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zkuser', to='zkcluster.Terminal')),
            ],
        ),
    ]
