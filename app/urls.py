from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('rendertopdf', views.render_to_pdf, name= 'rendertopdf')
    #path('attestation', views.attestation, name='attestation'),
    # path('venue_pdf', views.venue_pdf, name="venue_pdf"),

]
