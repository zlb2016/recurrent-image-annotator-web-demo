# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_predicted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_path', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('label', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='annotation',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotation.Image'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='labels',
            field=models.ManyToManyField(to='annotation.Label'),
        ),
    ]