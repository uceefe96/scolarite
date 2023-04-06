from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('rendertopdf', views.render_to_pdf, name= 'rendertopdf'),
    path('rendertopdf1', views.render_to_pdf1, name= 'rendertopdf1'),

]
