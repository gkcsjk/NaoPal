# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 05:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MotionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('len', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customize',
            fields=[
                ('motion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='robot.Motion')),
                ('file_path', models.FileField(upload_to='uploads/')),
                ('loops', models.IntegerField(default=500)),
            ],
        ),
        migrations.CreateModel(
            name='Lay',
            fields=[
                ('motion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='robot.Motion')),
            ],
        ),
        migrations.CreateModel(
            name='Rest',
            fields=[
                ('motion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='robot.Motion')),
            ],
        ),
        migrations.CreateModel(
            name='Speak',
            fields=[
                ('motion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='robot.Motion')),
                ('text', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('motion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='robot.Motion')),
            ],
        ),
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('motion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='robot.Motion')),
                ('vertical', models.FloatField(default=0)),
                ('horizontal', models.FloatField(default=0)),
                ('angle', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='motion',
            name='list_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='robot.MotionList'),
        ),
    ]