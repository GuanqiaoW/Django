# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataInfo', '0002_auto_20160712_0922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'permissions': (('can_drive', 'Can drive'),)},
        ),
    ]
