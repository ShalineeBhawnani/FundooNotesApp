# from __future__ import absolute_import, unicode_literals
# from project.celery import celery_app
# from celery import shared_task
# from django.core.mail import send_mail
# from celery.schedules import crontab
# from celery.task import periodic_task
# from datetime import timedelta
# from django.contrib.auth.models import User
# from django.template.loader import render_to_string
# from django.contrib.sites.models import Site
# from project import lib
# from lib.emmiter import email_event
# from note.models import Note
# from django.utils import timezone

# @shared_task
# def add(x, y):
#     return x + y

# @shared_task
# def count_reminder():
#     return Note.objects.count()

# @shared_task
# def task_send_email_for_reminder(user_id, title, pk):
#     user = User.objects.get(pk=user_id)
#     current_site = Site.objects.get_current()

#     message = render_to_string('reminder.html', {
#         'name': user.username,
#         'title': title,
#         'domain': current_site.domain,
#         'note_id': pk
#     })

#     recipient_list = [user.email, ]
#     email_event.emit("reminder_event", message, recipient_list)


# @shared_task
# def task_check_reminder():
#     notes = Note.objects.filter(reminder__isnull=False)
#     for note in notes:
#         nextTime = timezone.now() + timezone.timedelta(minutes=1)
#         print("got reminder")
#         if timezone.now() <= note.reminder < nextTime:
#             task_send_email_for_reminder.delay(note.user_id, note.title, note.pk)


