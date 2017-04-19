# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Motion)
admin.site.register(MotionList)
admin.site.register(Walk)
admin.site.register(Stand)
admin.site.register(Rest)
admin.site.register(Speak)
admin.site.register(Lay)
admin.site.register(Customize)