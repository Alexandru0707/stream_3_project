# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-18 15:18
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]