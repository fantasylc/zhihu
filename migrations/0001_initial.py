# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('question', models.CharField(verbose_name='问题', max_length=200)),
                ('question_link', models.CharField(verbose_name='问题链接', max_length='300')),
                ('author', models.CharField(verbose_name='答题者', default='匿名用户', max_length=200)),
                ('author_link', models.CharField(verbose_name='作者链接', max_length=300)),
                ('vote', models.IntegerField(verbose_name='赞同数')),
                ('summary', models.TextField(verbose_name='概述')),
                ('summary_img', models.CharField(max_length=500, verbose_name='概述图', default=None, null=True, blank=True)),
                ('answer', models.TextField(verbose_name='答案')),
                ('date', models.DateField(verbose_name='更新时间', auto_now=True)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': '知乎',
                'verbose_name_plural': '知乎',
            },
        ),
    ]
