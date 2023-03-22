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



@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    feed = []

    feed_list = list(chain(*feed))

    
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



@login_required(login_url='signin')
@csrf_exempt
def render_to_pdf(request):
    # profiles  = Profile.objects.all()
    profile = request.user.profile
    modules = Module.objects.filter(profile=profile)
    date = datetime.now().strftime('%d-%m-%Y')

    template_path = 'attestation.html'
    context = {'profile': profile, 'modules': modules, 'date': date}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="profile.pdf"'

    template =get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF Creation Failed', status=500)
    return response
