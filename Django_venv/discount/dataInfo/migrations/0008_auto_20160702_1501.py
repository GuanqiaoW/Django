# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dataInfo', '0007_auto_20160702_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_column='last_login'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staff',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, auto_now=True, db_column='last_login'),
            preserve_default=True,
        ),
    ]
