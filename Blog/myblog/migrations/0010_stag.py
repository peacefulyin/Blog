# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_auto_20170904_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='STag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('artical', models.ManyToManyField(to='myblog.Artical', null=True, blank=True)),
            ],
        ),
    ]
