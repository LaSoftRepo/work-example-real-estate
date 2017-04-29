# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0005_passbuildplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairBuildPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='\u0420\u0435\u043c\u043e\u043d\u0442 \u043d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u0438', editable=False, max_length=30, unique=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('title', models.TextField(blank=True, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('image', models.ImageField(blank=True, upload_to='background/%Y/%m/%d/', verbose_name='\u0424\u043e\u0442\u043e')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u043c\u043e\u043d\u0442 \u043d\u0435\u0434\u0432\u0438\u0436\u0438\u043c\u043e\u0441\u0442\u0438',
            },
        ),
    ]
