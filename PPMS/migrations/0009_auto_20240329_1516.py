# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-03-29 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PPMS', '0008_auto_20240329_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='customer_id',
            new_name='customer',
        ),
    ]