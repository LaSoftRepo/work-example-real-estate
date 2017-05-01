# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170501_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('description', models.TextField(verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439')),
                ('title_image', models.ImageField(blank=True, upload_to='result/%Y/%m/%d/', verbose_name='\u0424\u043e\u0442\u043e \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('image', models.ImageField(blank=True, upload_to='result/%Y/%m/%d/', verbose_name='\u0424\u043e\u0442\u043e \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442',
                'verbose_name_plural': '\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b',
            },
        ),
        migrations.AlterField(
            model_name='polls',
            name='questions',
            field=models.ManyToManyField(related_name='polls', to='polls.Question', verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441\u044b'),
        ),
        migrations.AddField(
            model_name='polls',
            name='results',
            field=models.ManyToManyField(related_name='polls', to='polls.Result', verbose_name='\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b'),
        ),
    ]
