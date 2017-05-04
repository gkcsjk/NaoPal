# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
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
    ml = MotionList.objects.order_by('list_name')
    allmo = Motion.objects.order_by('order')
    battery = src.get_battery()
    volume = 100*src.get_volume()
    cur=""

    context = {
        'ml': ml,
        'battery': battery,
        'volume': volume,
    }

    if request.POST.get('motionList'):
        name = request.POST.get('motionListName')
        if len(name) == 0:
            return HttpResponse('Can not be empty!')
        else:
            motionList = MotionList()
            motionList.list_name = name
            motionList.len = 0
            motionList.save()

    # Return motions in current selected motion list
    if request.POST.get('motionListSubmit'):
        mo = []
        for motion in allmo:
            if str(motion.list_id.list_name) == str(request.POST.get('options')):
                mo.append(motion)
        context['mo'] = mo
        cur = request.POST.get('options')
        context['cur'] = cur

    if request.POST.get('motionSubmit'):
        # TODO: check robot range (walk distance and angle)
        type = request.POST.get('motionOptions')
        cur = request.POST.get('cur')
        myMotionList = MotionList.objects.get(list_name=cur)
        myMotionList.len += 1
        myMotionList.save()
        myMotion = Motion()
        myMotion.motion_type = type
        myMotion.list_id = myMotionList
        myMotion.order = myMotionList.len-1
        myMotion.save()
        mo = []
        for motion in allmo:
            if str(motion.list_id.list_name) == cur:
                mo.append(motion)
        context['mo'] = mo
        context['cur'] = cur

        if type == "walk":
            x = request.POST.get('horizontal')
            y = request.POST.get('vertical')
            angle = request.POST.get('angle')
            myWalk = Walk()
            myWalk.motion = myMotion
            myWalk.vertical = y
            myWalk.horizontal = x
            myWalk.angle = angle
            myWalk.save()

        elif type == "rest":
            myRest = Rest()
            myRest.motion = myMotion
            myRest.save()

        elif type == "customize":
            myCustomize = Customize()
            myCustomize.motion = myMotion
            myCustomize.file_path = src.record(str(myMotion.id)+'.csv')
            myCustomize.save()

        elif type == "speak":
            text = request.POST.get('text')
            mySpeak = Speak()
            mySpeak.motion = myMotion
            mySpeak.text = text
            mySpeak.save()

        elif type == "stand":
            myStand = Stand()
            myStand.motion = myMotion
            myStand.save()

        elif type == "lay":
            myLay = Lay()
            myLay.motion = myMotion
            myLay.save()

    if request.POST.get('runSubmit'):
        cur = request.POST.get('cur')
        myMotionList = MotionList.objects.get(list_name=cur)
        q1 = Motion.objects.filter(list_id=myMotionList)
        q1 = q1.order_by('order')
        for obj in q1:
            if obj.motion_type == 'walk':
                x = obj.walk.horizontal
                y = obj.walk.vertical
                angle = obj.walk.angle
                src.walk(y, x, angle)
            elif obj.motion_type == 'rest':
                src.rest()
            elif obj.motion_type == 'stand':
                src.stand()
            elif obj.motion_type == 'lay':
                src.lay()
            elif obj.motion_type == 'customize':
                csv_path = obj.customize.file_path
                src.replay(csv_path)
            elif obj.motion_type == 'speak':
                text = str(obj.speak.text)
                src.speak(text)

    if request.POST.get('deleteList'):
        cur = request.POST.get('cur')
        myMotionList = MotionList.objects.get(list_name=cur)
        myMotionList.delete()

    if request.POST.get('deleteId'):
        cur = request.POST.get('cur')
        deleteId = request.POST.get('deleteId')
        myMotion = Motion.objects.get(pk=deleteId)
        myMotionList = MotionList.objects.get(list_name=cur)
        q1 = Motion.objects.filter(list_id=myMotionList, order__gt=myMotion.order)
        for e in q1:
            eMotion = Motion.objects.get(pk=e.pk)
            eMotion.order -= 1
            eMotion.save()
        myMotion.delete()

    if request.POST.get('index'):
        index = int(request.POST.get('index'))
        moveId = int(request.POST.get('moveId'))
        cur = request.POST.get('cur')
        myMotionList = MotionList.objects.get(list_name=cur)
        moveItem = Motion.objects.get(pk=moveId)
        old_index = moveItem.order
        print moveItem.order

        # move down
        if index > old_index:
            print "move down"
            q1 = Motion.objects.filter(list_id=myMotionList, order__gt=old_index, order__lte=index)
            for e in q1:
                myMotion = Motion.objects.get(pk=e.pk)
                myMotion.order -= 1
                myMotion.save()

        # move up
        elif index < old_index:
            print "move up"
            q2 = Motion.objects.filter(list_id=myMotionList, order__gte=index, order__lt=old_index)
            for e in q2:
                print e.order
                myMotion = Motion.objects.get(pk=e.pk)
                myMotion.order += 1
                myMotion.save()

        moveItem.order = index
        moveItem.save()
        print moveItem.order

    return render(request, 'timeline.html', context)





