from __future__ import absolute_import, unicode_literals
from project.celery import celery_app
from celery import shared_task
from .models import Note
from django.core.mail import send_mail
from celery.schedules import crontab
from celery.task import periodic_task
from datetime import timedelta

@shared_task
def add(x, y):
    return x + y

@shared_task
def count_reminder():
    return Note.objects.count()

@shared_task
def send_mail(self,request):
    user = request.user
    user_id = user.id
    print(user_id)
    note_obj = Note.objects.filter(user_id=user_id)
    print(note_obj)
    reminderlist = []
    completedlist = []
    for i in range(len(note_obj.values())):
        if note_obj.values()[i]['reminder'] is None:
            continue
        elif timezone.now() > note_obj.values()[i]['reminder']:
            completedlist.append(note_obj.values()[i])
        else:
            reminderlist.append(note_obj.values()[i])
    remid = {
        'reminder': reminderlist,
        'compl': completedlist
    }
    remdstr = str(remid)
    logger.info("Reminders data is loaded for %s", user)
    return HttpResponse(note_obj.values(), status=200)

