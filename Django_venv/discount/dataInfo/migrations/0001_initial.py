# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.BooleanField(default=True, choices=[(True, 'Male'), (False, 'Female')])),
                ('birthday', models.DateField(default=None)),
                ('created', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100, blank=True)),
                ('published_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('old_price', models.DecimalField(max_digits=1000, decimal_places=2)),
                ('new_price', models.DecimalField(max_digits=1000, decimal_places=2)),
                ('discount_start', models.DateField()),
                ('discount_end', models.DateField()),
                ('created', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('product_id', models.ForeignKey(default=1, to='dataInfo.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.BooleanField(default=True, choices=[(True, 'Male'), (False, 'Female')])),
                ('birthday', models.DateField(default=None)),
                ('created', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('authorized', models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.TextField()),
                ('street', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('longtitude', models.DecimalField(max_digits=999, decimal_places=6)),
                ('latitiude', models.DecimalField(max_digits=999, decimal_places=6)),
                ('created', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='staff',
            name='store_id',
            field=models.ForeignKey(default=1, to='dataInfo.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sale',
            name='store_id',
            field=models.ForeignKey(default=1, to='dataInfo.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='store_id',
            field=models.ForeignKey(default=1, to='dataInfo.Store'),
            preserve_default=True,
        ),
    ]
