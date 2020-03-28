from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from snippets.models import Profile,Registration


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print("created")
        Profile.objects.create(user=instance)
        print("created",user)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    print("save")
    instance.profile.save()