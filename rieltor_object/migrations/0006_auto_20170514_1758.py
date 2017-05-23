# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor_object', '0005_auto_20170510_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='\u0418\u043c\u044f')),
            ],
            options={
                'verbose_name': '\u0418\u043c\u044f',
                'verbose_name_plural': '\u0418\u043c\u0435\u043d\u0430',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=250, unique=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
            ],
            options={
                'verbose_name': '\u0422\u0435\u043b\u0435\u0444\u043e\u043d',
                'verbose_name_plural': '\u0422\u0435\u043b\u0435\u0444\u043e\u043d',
            },
        ),
        migrations.AddField(
            model_name='building',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='building', to='rieltor_object.Name', verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AddField(
            model_name='building',
            name='phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='building', to='rieltor_object.Phone', verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AddField(
            model_name='daily',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daily', to='rieltor_object.Name', verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AddField(
            model_name='daily',
            name='phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daily', to='rieltor_object.Phone', verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AddField(
            model_name='earth',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='earth', to='rieltor_object.Name', verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AddField(
            model_name='earth',
            name='phone1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='earth', to='rieltor_object.Phone', verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AddField(
            model_name='newbuilding',
            name='name1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='newbuilding', to='rieltor_object.Name', verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AddField(
            model_name='newbuilding',
            name='phone1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='newbuilding', to='rieltor_object.Phone', verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AddField(
            model_name='ofice',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ofice', to='rieltor_object.Name', verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AddField(
            model_name='ofice',
            name='phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ofice', to='rieltor_object.Phone', verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
    ]