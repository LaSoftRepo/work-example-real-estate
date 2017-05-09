# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DownBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(blank=True, null=True, verbose_name='\u041a\u043e\u0434 \u0431\u0430\u043d\u043d\u0435\u0440\u0430')),
                ('active_code', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='banner/%Y/%m/%d/', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('link', models.URLField(blank=True, help_text='http://example.com', null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u041d\u0438\u0436\u043d\u0438\u0439 \u0431\u0430\u043d\u043d\u0435\u0440',
            },
        ),
        migrations.CreateModel(
            name='SideBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(blank=True, null=True, verbose_name='\u041a\u043e\u0434 \u0431\u0430\u043d\u043d\u0435\u0440\u0430')),
                ('active_code', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='banner/%Y/%m/%d/', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('link', models.URLField(blank=True, help_text='http://example.com', null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u0411\u043e\u043a\u043e\u0432\u043e\u0439 \u0431\u0430\u043d\u043d\u0435\u0440',
            },
        ),
    ]