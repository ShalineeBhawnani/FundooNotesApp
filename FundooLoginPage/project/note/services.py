# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# import os
# class MailServices():

#     @staticmethod
#     def send_reminder(user, note):

#         subject = f'Reminder for note {note.title}'
#         from_email = os.getenv('EMAIL_HOST_USER')
#         to_email = ['shalieebhawnani90@gmail.com']
#         message = render_to_string('reminder.html', {
#             'user': user,
#             'note': note,
#         })
#         send_mail(subject, message, from_email, to_email, fail_silently=True)

