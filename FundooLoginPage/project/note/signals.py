from django.db.models.signals import post_save
from django.dispatch import receiver
from note.tasks import send_email
from note.model import Note
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_reminder(sender, instance, created, **kwargs):
    if created:
        task = send_email(username=instance.first_name, id=instance.id, hash=instance.hash,
                                 email=instance.email)
        task.delay()
        
@receiver(post_save, sender=User)     
def update_reminder(sender, instance, **kwargs):
    instance.reminder.save()

