# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_apartmentnext'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartmentnext',
            options={'ordering': ['-id'], 'verbose_name': '\u0420\u044f\u0434\u043e\u043c \u0441 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u043e\u0439', 'verbose_name_plural': '\u0420\u044f\u0434\u043e\u043c \u0441 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u043e\u0439'},
        ),
        migrations.AlterField(
            model_name='apartmentnext',
            name='name',
            field=models.CharField(max_length=250, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]
