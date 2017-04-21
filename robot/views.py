# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
import src
# Create your views here.


def show_index(request):
    if request.GET.get('walk_submit'):
        x = float(request.GET.get('x'))
        y = float(request.GET.get('y'))
        angle = float(request.GET.get('angle'))
        motion = Motion()
        walk = Walk()

        walk.horizontal = x
        walk.vertical = y
        walk.angle = angle
        walk.save()
        return render(request, 'index.html', {})

    else:
        return render(request, 'index.html', {})

def show_timeline(request):



    return render(request, 'timeline.html', {})