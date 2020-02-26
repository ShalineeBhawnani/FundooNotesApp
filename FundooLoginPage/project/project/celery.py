from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from .settings import CELERY_BROKER_URL
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

celery_app = Celery('project', broker=CELERY_BROKER_URL)
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
celery_app.conf.beat_schedule = {'add-every-05-seconds':
                                   {'task': 'note.tasks.send_mail_task', 
                                    'schedule': 05.0, }, }


@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# @celery_app.task
# def send_mail(x, y):
#     return x + y

