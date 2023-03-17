from django.contrib import admin
from .models import Profile, Module, Filiere

# Register your models here.
admin.site.register(Profile)
admin.site.register(Module)
admin.site.register(Filiere)