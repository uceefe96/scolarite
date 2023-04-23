from django.contrib import admin
from .models import Profile, Module, Filiere, Attestationrequest, Handicap, Sex, Bac, Semestre, Attestation, Mention 

# Register your models here.
admin.site.register(Profile)
admin.site.register(Module)
admin.site.register(Filiere)
admin.site.register(Attestationrequest)
admin.site.register(Mention)
admin.site.register(Handicap)
admin.site.register(Sex)
admin.site.register(Semestre)
admin.site.register(Attestation)






