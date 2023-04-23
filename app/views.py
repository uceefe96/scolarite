from datetime import datetime
from itertools import chain
import base64
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views import View
from django.utils.decorators import method_decorator
from .models import Profile, Module, Attestationrequest, Attestation
from xhtml2pdf import pisa
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
import barcode
from barcode.writer import ImageWriter
from barcode import Code128
import qrcode
import io
from django.http import HttpResponse
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from project import settings




def signup(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')




@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    return render(request, 'index.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def settings(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile': profile})




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
@csrf_exempt
def attestationscolarite(request):

    Attestationrequest.objects.create(user=request.user)
    profile = request.user.profile
    date = datetime.now().strftime('%d-%m-%Y')
    # module = Module.objects.filter(profile=profile)
    context = {'profile': profile, 'date': date} #, 'module': module
    
    

    template_path = 'attestation_scolarite.html'
    #
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="profile.pdf"'

    template =get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF Creation Failed', status=500)
    return response



@login_required(login_url='signin')
@csrf_exempt
def attestationreinscription(request):
    # attestation = Attestation.objects.create(user=request.user)
    Attestationrequest.objects.create(user=request.user)
    
    profile = request.user.profile
    
    date = datetime.now().strftime('%d-%m-%Y')
    context = {'profile': profile, 'date': date} #, 'barcode_path': barcode.save('media/barcodes/{}'.format(barcode_value))
    
    


    template_path = 'attestation.html'
    
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="profile.pdf"'

    template =get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF Creation Failed', status=500)
    return response



# import os

# @login_required(login_url='signin')
# @csrf_exempt
# def attestationreinscription(request):
    
#     Attestationrequest.objects.create(user=request.user)
    
#     profile = request.user.profile
    
#     date = datetime.now().strftime('%d-%m-%Y')
#     context = {'profile': profile, 'date': date}
    
#     # Génération du code QR
#     qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
#     qr.add_data("@login_required(login_url='signin')\n@csrf_exempt\ndef attestationreinscription(request):\n    Attestationrequest.objects.create(user=request.user)\n    profile = request.user.profile\n    date = datetime.now().strftime('%d-%m-%Y')\n    context = {'profile': profile, 'date': date}\n    template_path = 'attestation.html'\n    response = HttpResponse(content_type='application/pdf')\n    response['Content-Disposition'] = 'filename=\"profile.pdf\"'\n    template = get_template(template_path)\n    html = template.render(context)\n    pisa_status = pisa.CreatePDF(html, dest=response)\n    if pisa_status.err:\n        return HttpResponse('PDF Creation Failed', status=500)\n    return response")
#     qr.make(fit=True)
#     qr_image = qr.make_image(fill_color="black", back_color="white")

#     # Enregistrement de l'image QR dans le dossier qrcode_image
#     qr_image_path = os.path.join(settings.MEDIA_ROOT, 'media/qrcode_image', 'qrcode.png')
#     qr_image.save(qr_image_path)

#     # Conversion de l'image en base64
#     with open(qr_image_path, 'rb') as f:
#         qr_image_base64 = base64.b64encode(f.read()).decode('utf-8')

#     context['qrcode_image'] = 'data:image/png;base64,{}'.format(qr_image_base64)
#     template = loader.get_template('attestation.html')
#     html = template.render(context)
    
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="profile.pdf"'
    
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('PDF Creation Failed', status=500)
    
#     return response