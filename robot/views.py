# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import src
# Create your views here.

def show_index(request):
    return render(request, 'index.html', {})

def show_timeline(request):
    return render(request, 'timeline.html', {})