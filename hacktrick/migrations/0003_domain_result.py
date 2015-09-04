# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0002_domain_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='result',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
