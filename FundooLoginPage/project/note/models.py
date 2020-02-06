from django.db import models
from django.contrib.auth.models import User

class Label(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='label_owner')
    label = models.CharField(max_length=25)

    def __str__(self):
        return str(self.label)


class Note(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user"
    )
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=250)
    note_image = models.ImageField(upload_to='images/', blank=True, null=True)
    label = models.ManyToManyField(Label)
    date_posted = models.DateTimeField(auto_now_add=True)
    collaborators = models.ManyToManyField(User, blank=True)
    is_archived = models.BooleanField(default=False)
    is_trashed = models.BooleanField(default=False)
    color = models.CharField(max_length=16, blank=True)
    is_pinned = models.BooleanField(default=False)
    link = models.URLField(blank=True, null=True)
    reminder = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

