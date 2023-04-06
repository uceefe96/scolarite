from django.contrib import admin
from .models import Profile, Module, Filiere,Attestationrequest 

# Register your models here.
admin.site.register(Profile)
admin.site.register(Module)
admin.site.register(Filiere)
admin.site.register(Attestationrequest)

