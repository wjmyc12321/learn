# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-24 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
