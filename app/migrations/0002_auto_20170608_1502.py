# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='due_date',
            field=models.DateField(verbose_name='*Due Date'),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(help_text='Enter the name of the List', max_length=50, verbose_name='*Name'),
        ),
        migrations.AlterField(
            model_name='list',
            name='priority',
            field=models.IntegerField(verbose_name='*Priority'),
        ),
        migrations.AlterField(
            model_name='task',
            name='completed_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='note',
            field=models.TextField(null=True),
        ),
    ]
