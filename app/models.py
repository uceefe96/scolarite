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
    cne = models.CharField(max_length=100, blank=True)
    nom = models.CharField(max_length=100, blank=True)
    prenom = models.CharField(max_length=100, blank=True)
    date_naissance = models.DateField(null=True)
    lieu_naissance = models.CharField(max_length=100, blank=True)
    filier = models.ForeignKey(Filiere, on_delete=models.CASCADE, blank='')
    def __str__(self):
        return self.user.username


# class Attestation(models.Model):
#     # Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='attestations', null= True)
#     cin = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='attestations_cin', null= True)
#     cne = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='attestations_cne', null= True)
#     nom = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='attestations_nom', null= True)
#     prenom = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='attestations_prenom', null= True)
#     date = models.DateTimeField()
#     # def __str__(self):
#     #     return self.Profile

# class Attestation(models.Model):
#     cin = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='attestations_cin', null= True)
#     cne = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='attestations_cne', null= True)
#     nom = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='attestations_nom', null= True)
#     prenom = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='attestations_prenom', null= True)
#     date = models.DateTimeField()
    


class Module(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    module = models.CharField(max_length=50)
    note = models.DecimalField(max_digits=6, decimal_places=3)
    def __str__(self):
        return f"{self.profile.user.username} - {self.module}"


