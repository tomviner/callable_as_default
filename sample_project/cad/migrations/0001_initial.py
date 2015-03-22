# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import cad.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=cad.models.get_title, max_length=10)),
            ],
        ),
    ]
