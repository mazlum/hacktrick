# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0004_auto_20150904_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('port', models.IntegerField()),
                ('protocol', models.CharField(max_length=5)),
                ('state', models.CharField(max_length=10)),
                ('service', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='domain',
            name='up',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='port',
            name='domain',
            field=models.ForeignKey(to='hacktrick.Domain'),
        ),
    ]
