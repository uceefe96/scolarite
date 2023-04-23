from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('attestationreinscription', views.attestationreinscription, name= 'attestationreinscription'),
    path('attestationscolarite', views.attestationscolarite, name= 'attestationscolarite'),

]
