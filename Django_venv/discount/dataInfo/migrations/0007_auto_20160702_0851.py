# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataInfo', '0006_auto_20160702_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='_last_login',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='_last_login',
        ),
    ]
