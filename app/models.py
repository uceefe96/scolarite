from django.db import models

from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.contrib.auth.models import User


class Handicap(models.Model):
    idhandicap = models.AutoField(db_column='idHandicap', primary_key=True)  # Field name made lowercase.
    handicap = models.CharField(db_column='Handicap', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'handicap'
    def __str__(self):
        return self.handicap



class Sex(models.Model):
    idsex = models.AutoField(db_column='idSEX', primary_key=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sex'
    def __str__(self):
        return self.sex    



class Bac(models.Model):
    idbac = models.AutoField(db_column='idBAC', primary_key=True)  # Field name made lowercase.
    bac = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bac'
    def __str__(self):
        return self.bac     



class Attestation(models.Model):
    idattestation = models.AutoField(primary_key=True)
    attestation = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attestation'

    def __str__(self):
        return self.attestation

class Filiere(models.Model):
    idfiliere = models.AutoField(db_column='idFiliere', primary_key=True)  # Field name made lowercase.
    nomfiliere = models.CharField(db_column='nomFiliere', max_length=45, blank=True, null=True)  # Field name made lowercase.       
    intitulefiliere = models.CharField(db_column='intituleFiliere', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'filiere'
    def __str__(self):
        return self.intitulefiliere     


class Semestre(models.Model):
    idsemestre = models.AutoField(primary_key=True)
    semestre = models.CharField(max_length=45, blank=True, null=True)
    idFiliere = models.ForeignKey(Filiere, models.DO_NOTHING, db_column='idF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'semestre'
    def __str__(self):
        return self.semestre 


class Module(models.Model):
    profileid = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profileid', blank=True, null=True,related_name='modules')
    module = models.CharField(max_length=45, blank=True, null=True)
    idfiliere = models.ForeignKey(Filiere, models.DO_NOTHING, db_column='idfiliere', blank=True, null=True)
    note = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    idsemestre = models.IntegerField(db_column='IdSemestre', blank=True, null=True)  # Field name made lowercase.    validation = models.CharField(max_length=45, blank=True, null=True)
    session = models.CharField(max_length=45, blank=True, null=True)
    validation = models.CharField(max_length=45, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'module'

    def __str__(self):
        return self.module


class Mention(models.Model):
    idmention = models.AutoField(primary_key=True)
    mention = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mention'
    def __str__(self):
        return self.mention   

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
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')#profileimg = models.TextField(blank=True, null=True)
    # modules = models.ManyToManyField(Module, through='Note')
    tel = models.IntegerField(db_column='Tel', blank=True, null=True)  # Field name made lowercase.
    obtionbac = models.CharField(max_length=45, blank=True, null=True)
    mail = models.CharField(max_length=45, blank=True, null=True)
    mailacademique = models.CharField(max_length=45, blank=True, null=True)
    idbac = models.ForeignKey(Bac, models.DO_NOTHING, db_column='idbac', blank=True, null=True)
    idmention = models.ForeignKey(Mention, models.DO_NOTHING, db_column='idmention', blank=True, null=True)
    arabicnam = models.CharField(max_length=45, blank=True, null=True)
    arabiclieunaissance = models.CharField(max_length=45, blank=True, null=True)
    idsex = models.ForeignKey('Sex', models.DO_NOTHING, db_column='idsex', blank=True, null=True)
    idhandicap = models.ForeignKey(Handicap, models.DO_NOTHING, db_column='idhandicap', blank=True, null=True)
    pays = models.CharField(db_column='Pays', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=100, blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'profile'
    def __str__(self):
        return self.user.username    




class Attestationrequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_request = models.DateTimeField(auto_now_add=True)
    attestation = models.ForeignKey(Attestation, models.DO_NOTHING, db_column='attestation', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attestationrequest'

    def __str__(self):
        return f"{self.user.profile.cne} | {self.user.profile.nom} | {self.user.profile.prenom} | {self.user.profile.filiere} | {self.attestation.attestation if self.attestation else ''} | {self.date_request}  "
