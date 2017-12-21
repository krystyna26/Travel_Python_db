# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-27 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_trips', to='tb.User'),
        ),
    ]