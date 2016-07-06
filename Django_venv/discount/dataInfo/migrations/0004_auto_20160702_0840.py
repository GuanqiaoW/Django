# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataInfo', '0003_auto_20160702_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='_is_active',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='_last_login',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='_is_active',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='_last_login',
        ),
    ]
