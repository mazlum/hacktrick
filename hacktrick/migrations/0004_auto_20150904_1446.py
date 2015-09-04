# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0003_domain_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='result',
            field=models.TextField(null=True, blank=True),
        ),
    ]
