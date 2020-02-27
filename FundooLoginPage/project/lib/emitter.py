from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from pyee import BaseEventEmitter

from project import settings
from project.settings import EMAIL_HOST_USER

ee = BaseEventEmitter()


@ee.on('send_email')
def send_email(recipientemail, mail_message):

    subject, from_email, to = 'greeting', settings.EMAIL_HOST, recipientemail
    msg = EmailMultiAlternatives(subject, mail_message, from_email, [to])
    msg.attach_alternative(mail_message, "text/html")
    msg.send()
    
from django.core.mail import EmailMultiAlternatives

from django.conf import settings
from pymitter import EventEmitter

email_event = EventEmitter()

@email_event.on("reminder_event")
def email_for_reset_password(message, recipient_list):
    email_from = settings.EMAIL_HOST_USER
    subject = 'reminder for you'
    msg = EmailMultiAlternatives(subject=subject, from_email=email_from,
                                 to=recipient_list, body=message)
    msg.attach_alternative(message, "text/html")
    msg.send()
