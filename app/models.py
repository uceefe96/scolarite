from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.

class Filiere(models.Model):
    filier = models.CharField(max_length=50)
    def __str__(self):
        return self.filier



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # id_user = models.IntegerField()
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    cin = models.CharField(max_length=100, blank=True)
    filier = models.ForeignKey(Filiere, on_delete=models.CASCADE, blank='')
    def __str__(self):
        return self.user.username


class Module(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    module = models.CharField(max_length=50)
    note = models.DecimalField(max_digits=6, decimal_places=3)
    def __str__(self):
        return f"{self.profile.user.username} - {self.module}"


