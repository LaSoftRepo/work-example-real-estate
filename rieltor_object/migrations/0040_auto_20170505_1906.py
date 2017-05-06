# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor_object', '0039_auto_20170425_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='appointment',
            field=models.CharField(blank=True, choices=[('apartment', '\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u0430'), ('house', '\u0414\u043e\u043c')], max_length=20, null=True, verbose_name='\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='building',
            name='entrance',
            field=models.CharField(blank=True, choices=[('facade', '\u0424\u0430\u0441\u0430\u0434'), ('from_yard', '\u0421\u043e \u0434\u0432\u043e\u0440\u0430'), ('with_grand', '\u0421 \u043f\u0430\u0440\u0430\u0434\u043d\u043e\u0439')], max_length=20, null=True, verbose_name='\u0412\u0445\u043e\u0434'),
        ),
        migrations.AlterField(
            model_name='building',
            name='floor',
            field=models.CharField(blank=True, choices=[('first', '1-\u0439'), ('base', '\u0426\u043e\u043a\u043e\u043b\u044c'), ('mezzanine', '\u0411\u0435\u043b\u044c\u044d\u0442\u0430\u0436')], max_length=20, null=True, verbose_name='\u042d\u0442\u0430\u0436'),
        ),
        migrations.AlterField(
            model_name='building',
            name='location',
            field=models.CharField(blank=True, choices=[('facade', '\u0424\u0430\u0441\u0430\u0434'), ('from_yard', '\u0414\u0432\u043e\u0440\u043e\u0432\u043e\u0439'), ('business_center', '\u0411\u0438\u0437\u043d\u0435\u0441-\u0446\u0435\u043d\u0442\u0440')], max_length=20, null=True, verbose_name='\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='building',
            name='status',
            field=models.CharField(blank=True, choices=[('vip', 'VIP'), ('default', '\u041e\u0431\u044b\u0447\u043d\u043e\u0435'), ('short', '\u041a\u0440\u0430\u0442\u043a\u043e\u0435')], max_length=20, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441'),
        ),
        migrations.AlterField(
            model_name='building',
            name='type_deal',
            field=models.CharField(blank=True, choices=[('rent', '\u0410\u0440\u0435\u043d\u0434\u0430'), ('sale', '\u041f\u0440\u043e\u0434\u0430\u0436\u0430')], max_length=20, null=True, verbose_name='\u0422\u0438\u043f'),
        ),
        migrations.AlterField(
            model_name='earth',
            name='communication',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('water', '\u0412\u043e\u0434\u0430'), ('gas', '\u0413\u0430\u0437'), ('sewage', '\u041a\u0430\u043d\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f'), ('electricity', '\u042d\u043b\u0435\u043a\u0442\u0440\u0438\u0447\u0435\u0441\u0442\u0432\u043e')], max_length=50, null=True, verbose_name='\u041a\u043e\u043c\u043c\u0443\u043d\u0438\u043a\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='earth',
            name='structure_house',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('house', '\u0414\u043e\u043c'), ('cuisine', '\u041b\u0435\u0442\u043d\u0430\u044f \u043a\u0443\u0445\u043d\u044f'), ('barn', '\u0421\u0430\u0440\u0430\u0439'), ('pool', '\u0411\u0430\u0441\u0441\u0435\u0439\u043d')], max_length=50, null=True, verbose_name='\u0421\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0434\u043e\u043c\u0430'),
        ),
        migrations.AlterField(
            model_name='earth',
            name='type_area',
            field=models.CharField(blank=True, choices=[('for_building', '\u041f\u043e\u0434 \u0437\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0443'), ('gardening', '\u0421\u0430\u0434\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e'), ('commercial', '\u041a\u043e\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u0430\u044f'), ('handed', '\u0414\u043e\u043c \u0441\u0434\u0430\u043d')], max_length=50, null=True, verbose_name='\u0422\u0438\u043f \u0423\u0447\u0430\u0441\u0442\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='ofice',
            name='appointment',
            field=models.CharField(blank=True, choices=[('apartment', '\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u0430'), ('house', '\u0414\u043e\u043c')], max_length=20, null=True, verbose_name='\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='ofice',
            name='entrance',
            field=models.CharField(blank=True, choices=[('facade', '\u0424\u0430\u0441\u0430\u0434'), ('from_yard', '\u0421\u043e \u0434\u0432\u043e\u0440\u0430'), ('with_grand', '\u0421 \u043f\u0430\u0440\u0430\u0434\u043d\u043e\u0439')], max_length=20, null=True, verbose_name='\u0412\u0445\u043e\u0434'),
        ),
        migrations.AlterField(
            model_name='ofice',
            name='floor',
            field=models.CharField(blank=True, choices=[('first', '1-\u0439'), ('base', '\u0426\u043e\u043a\u043e\u043b\u044c'), ('mezzanine', '\u0411\u0435\u043b\u044c\u044d\u0442\u0430\u0436')], max_length=20, null=True, verbose_name='\u042d\u0442\u0430\u0436'),
        ),
        migrations.AlterField(
            model_name='ofice',
            name='location',
            field=models.CharField(blank=True, choices=[('facade', '\u0424\u0430\u0441\u0430\u0434'), ('from_yard', '\u0414\u0432\u043e\u0440\u043e\u0432\u043e\u0439'), ('business_center', '\u0411\u0438\u0437\u043d\u0435\u0441-\u0446\u0435\u043d\u0442\u0440')], max_length=20, null=True, verbose_name='\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='ofice',
            name='status',
            field=models.CharField(blank=True, choices=[('vip', 'VIP'), ('default', '\u041e\u0431\u044b\u0447\u043d\u043e\u0435'), ('short', '\u041a\u0440\u0430\u0442\u043a\u043e\u0435')], max_length=20, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441'),
        ),
        migrations.AlterField(
            model_name='ofice',
            name='type_deal',
            field=models.CharField(blank=True, choices=[('rent', '\u0410\u0440\u0435\u043d\u0434\u0430'), ('sale', '\u041f\u0440\u043e\u0434\u0430\u0436\u0430')], max_length=20, null=True, verbose_name='\u0422\u0438\u043f'),
        ),
    ]
