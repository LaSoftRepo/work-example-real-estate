# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 22:02
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin2', '0019_auto_20170506_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpagemodel',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='\u041a\u043e\u043d\u0442\u0435\u043d\u0442'),
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='background/%Y/%m/%d/', verbose_name='\u0424\u043e\u0442\u043e'),
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='image_seo',
            field=models.ImageField(blank=True, upload_to='seo/%Y/%m/%d/', verbose_name='\u0424\u043e\u0442\u043e SEO'),
        ),
        migrations.AddField(
            model_name='indexpagemodel',
            name='title_h1',
            field=models.TextField(blank=True, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a H1'),
        ),
        migrations.AlterField(
            model_name='buildingpagemodel',
            name='title',
            field=models.TextField(blank=True, null=True, verbose_name='SEO \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]
