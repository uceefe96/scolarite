from datetime import datetime
from itertools import chain
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views import View
from django.utils.decorators import method_decorator
from .models import Profile, Module #, Attestation
from xhtml2pdf import pisa
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt


# @login_required(login_url='signin')
# @csrf_exempt
# def venue_pdf(request):
#     # Create a bytestream buffer
#     buf = io.BytesIO()

#     # Create a canvas with the buffer and set its properties
#     c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

#     # Create a text object and set its properties
#     textob = c.beginText()
#     # textob.setTextOrigin(1 * inch, 10 * inch)  # Set the text origin to 1 inch from the left and 10 inches from the bottom
#     textob.setFont("Helvetica", 14)

#     # Get the profile of the logged-in user
#     profile = request.user.Profile

#     # Add the profile information to the text object
#     lines = [
#         f"CNE: {profile.cne}",
#         f"CIN: {profile.cin}",
#         f"Nom: {profile.nom}",
#         f"Prénom: {profile.prenom}",
#         f"Date de naissance: {profile.date_naissance}",
#         f"Lieu de naissance: {profile.lieu_naissance}",
#         f"Filière: {profile.filier}",
#         " ",  # Add a blank line at the end
#     ]

#     # Calculate the width of the longest line
#     max_width = max([c.stringWidth(line) for line in lines])
    
#     # Calculate the center of the page
#     page_center = settings.PAGE_WIDTH / 2.0

#     # Calculate the start position
#     start_x = page_center - (max_width / 2.0)
#     start_y = 10 * inch

#     # Set the text origin to the center of the page
#     textob.setTextOrigin(start_x, start_y)

#     for line in lines:
#         textob.textLine(line)

#     # Add the text object to the canvas and finish up
#     c.drawText(textob)
#     c.showPage()
#     c.save()

#     # Reset the buffer position to the beginning and return the response with the PDF file
#     buf.seek(0)
#     return FileResponse(buf, as_attachment=True, filename='venue.pdf')



# @login_required(login_url='signin')
# @csrf_exempt
# def venue_pdf(request):
#     # Create a bytestream buffer
#     buf = io.BytesIO()

#     # Create a canvas with the buffer and set its properties
#     c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

#     # Create a text object and set its properties
#     textob = c.beginText()
#     textob.setTextOrigin(1 * inch, 10 * inch)  # Set the text origin to 1 inch from the left and 10 inches from the bottom
#     textob.setFont("Helvetica", 14)

#     # Get the list of profiles from the database
#     profiles = Profile.objects.all()

#     # Loop over each profile and add its information to the text object
#     for profile in profiles:
#         lines = [
#             f"CNE: {profile.cne}",
#             f"CIN: {profile.cin}",
#             f"Nom: {profile.nom}",
#             f"Prénom: {profile.prenom}",
#             f"Date de naissance: {profile.date_naissance}",
#             f"Lieu de naissance: {profile.lieu_naissance}",
#             f"Filière: {profile.filier}",
#             " ",  # Add a blank line between each profile
#         ]
#         for line in lines:
#             textob.textLine(line)

#     # Add the text object to the canvas and finish up
#     c.drawText(textob)
#     c.showPage()
#     c.save()

#     # Reset the buffer position to the beginning and return the response with the PDF file
#     buf.seek(0)
#     return FileResponse(buf, as_attachment=True, filename='venue.pdf')








'''def venue_pdf(request):
    # Create bystestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize = letter, bottomup = 0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)


#     # Add some lines of text
    # lines = [
    #     "University",
    #     "date = datetime.now()"
    # ]
    profile = Profile.objects.all()

    lines = []

    for profile in Profile:
        lines.append(profile.cne)
        lines.append(profile.cin)
        lines.append(profile.nom)
        lines.append(profile.prenom)
        lines.append(profile.date_naissance)
        lines.append(profile.lieu_naissance)
        lines.append(profile.filier)
        lines.append("     ")
#     # Loop
#     # for line in lines:
#     #     textob.textLine(line)
    
#     # Finish up
    c.drawText(textob)  
    c.showPage()
    c.save()
    buf.seek(0) 
    return FileResponse(buf, as_attachment=True, filename='venue.pdf')

'''

# @login_required(login_url='signin')
# def attestation(request):
#     if request.method == 'POST':
#         cin = request.POST.get('cin')
#         cne = request.POST.get('cne')
#         nom = request.POST.get('nom')
#         prenom = request.POST.get('prenom')
#         date = datetime.now()
#         attestation = Attestation(cin=cin, cne=cne, nom=nom, prenom=prenom, date=date)
#         attestation.save()
#         return redirect('attestation')
#     else:
#         # Display the form
#         return render(request, 'attestation_form.html')

# @login_required(login_url='signin')
# def attestation(request):
#     cin = request.POST.get('cin')
#     cne = request.POST.get('cne')
#     nom = request.POST.get('nom')
#     prenom = request.POST.get('prenom')
#     date = datetime.now()
#     profile_cin = get_object_or_404(profile, id = cin)
#     profile_cne = get_object_or_404(profile, id = cne)
#     profile_nom = get_object_or_404(profile, id = nom)
#     profile_prenom = get_object_or_404(profile, id = prenom)
#     attestation = Attestation(cin=cin, cne=cne, nom=nom, prenom=prenom, date=date)
#     attestation.save()
#     return redirect('attestation')


@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    #user_attestation_list = []
    feed = []

    feed_list = list(chain(*feed))

    # user suggestion starts
    #all_attestations = #Attestation.objects.all()
    #user_attestations_all = []

    username_profile = []
    username_profile_list = []

    for ids in username_profile:
        profile_lists = Profile.objects.filter(user_id=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))

    return render(request, 'index.html', {'user_profile': user_profile, 'posts':feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4]})


@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)


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


# class AttestationPDF(View):
#     @method_decorator(login_required)
#     def get(self, request, pk):
#         profile = get_object_or_404(Profile, pk=pk)
#         modules = Module.objects.filter(profile=profile)
#         context = {'profile': profile, 'modules': modules}
#         template = 'attestation.html'
#         pdf = render_to_pdf(template, context)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Attestation_%s.pdf" % profile.user.username
#             content = "inline; filename=%s" % filename
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename=%s" % filename
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not Found")

@login_required(login_url='signin')
@csrf_exempt
def render_to_pdf(request):
    profiles  = Profile.objects.all()

    template_path = 'attestation.html'

    context = {'profiles' : profiles}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="profile.pdf"'

    template =get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF Creation Failed', status=500)
    return response

# class AttestationView(View):
#     @method_decorator(login_required)
#     def get(self, request, pk):
#         profile = get_object_or_404(Profile, pk=pk)
#         modules = Module.objects.filter(profile=profile)
#         context = {'profile': profile, 'modules': modules}
#         return render(request, 'attestation.html', context=context)
