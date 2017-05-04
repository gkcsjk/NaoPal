# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class MotionList(models.Model):
    list_name = models.CharField(max_length=50, primary_key=True)
    len = models.IntegerField(default=0)


class Motion(models.Model):
    motion_type = models.CharField(default='default motion', max_length=50)
    list_id = models.ForeignKey(MotionList, on_delete=models.CASCADE)
    order = models.IntegerField(default=1000)


class Walk(models.Model):
    motion = models.OneToOneField(Motion, on_delete=models.CASCADE, primary_key=True)
    vertical = models.FloatField(default=0)
    horizontal = models.FloatField(default=0)
    angle = models.FloatField(default=0)


class Customize(models.Model):
    motion = models.OneToOneField(Motion, on_delete=models.CASCADE, primary_key=True)
    file_path = models.FilePathField()
    loops = models.IntegerField(default=500)


class Speak(models.Model):
    motion = models.OneToOneField(Motion, on_delete=models.CASCADE, primary_key=True)
    text = models.CharField(max_length=1024)


class Stand(models.Model):
    motion = models.OneToOneField(Motion, on_delete=models.CASCADE, primary_key=True)


class Rest(models.Model):
    motion = models.OneToOneField(Motion, on_delete=models.CASCADE, primary_key=True)


class Lay(models.Model):
    motion = models.OneToOneField(Motion, on_delete=models.CASCADE, primary_key=True)


