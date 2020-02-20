                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
from django.db import models

#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save

class Registration(models.Model):
    
    fullname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 100)
    password2 = models.CharField(max_length = 100)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)