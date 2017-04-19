# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MotionList(models.Model):
    len = models.IntegerField(default=0)


class Motion(models.Model):
    list_id = models.ForeignKey(MotionList, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)


class Walk(models.Model):
    motion = models.OneToOneField(Motion, on_delete=models.CASCADE, primary_key=True)
    vertical = models.FloatField(default=0)
    horizontal = models.FloatField(default=0)
    angle = models.FloatField(default=0)

class Customize(models.Model):
    motion = models.OneToOneField(Motion, on_delete=models.CASCADE, primary_key=True)
    file_path = models.FileField(upload_to='uploads/')
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


