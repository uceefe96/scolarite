from django.db import models

from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.contrib.auth.models import User


class Attestationrequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_request = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'attestationrequest'
    def __str__(self):
        return f"{self.user.profile.cne} - {self.date_request}"

class Filiere(models.Model):
    idfiliere = models.AutoField(db_column='idFiliere', primary_key=True)  # Field name made lowercase.
    nomfiliere = models.CharField(db_column='nomFiliere', max_length=45, blank=True, null=True)  # Field name made lowercase.
    intitulefiliere = models.CharField(db_column='intituleFiliere', max_length=45, blank=True, null=True)  # Field name made lowercase.    

    class Meta:
        managed = False
        db_table = 'filiere'

    def __str__(self):
        return self.nomfiliere

class Module(models.Model):
    profileid = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profileid', blank=True, null=True)
    cne = models.CharField(max_length=45, blank=True, null=True)
    module = models.CharField(max_length=45, blank=True, null=True)
    # note = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module'

    def __str__(self):
        return self.module

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idprofile = models.AutoField(db_column='idProfile', primary_key=True)  # Field name made lowercase.
    cne = models.CharField(db_column='CNE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nom = models.CharField(max_length=45, blank=True, null=True)
    prenom = models.CharField(max_length=45, blank=True, null=True)
    cin = models.CharField(db_column='CIN', max_length=45, blank=True, null=True)  # Field name made lowercase.
    datenaissance = models.CharField(db_column='dateNaissance', max_length=45, blank=True, null=True)  # Field name made lowercase.        
    lieunaissance = models.CharField(db_column='lieuNaissance', max_length=45, blank=True, null=True)  # Field name made lowercase.        
    filiere = models.ForeignKey(Filiere, models.DO_NOTHING, db_column='filiere', blank=True, null=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    modules = models.ManyToManyField(Module, through='Note')

    class Meta:
        managed = False
        db_table = 'profile'
    def __str__(self):
        return self.user.username    
    
    

class Note(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        unique_together = ('profile', 'module')