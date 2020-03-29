from __future__ import absolute_import, unicode_literals
from celery import Celery
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from djcelery.models import PeriodicTask
import datetime
from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from celery.app.registry import TaskRegistry


# from .views import send_mail_user
# from notes.celery import app

app = Celery('tasks', broker='redis://localhost:6379')


@app.task
@periodic_task(run_every=(crontab(minute='*/1')), name="reminder", ignore_result=True)
def reminder():
    print("see you in 200 seconds")
    
    send_mail("Hi","Reminder",EMAIL_HOST_USER,['shalineebhawnani90@gmail.com'])
    # print(TaskRegistry.__dict__)
    print("done")
    return True

