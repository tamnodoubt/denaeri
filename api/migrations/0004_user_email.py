# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='default@default.com', max_length=200),
            preserve_default=False,
        ),
    ]