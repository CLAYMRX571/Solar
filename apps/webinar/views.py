from django.shortcuts import render, redirect
from .models import Webinar

def Webinarviews(request):
    webinar = Webinar.objects.all()  

    context = {
        'webinar': webinar,
    }

    return render(request, 'webinar.html', context)

def lan_switch_webinar(request, lan):
    return redirect(f'/{lan}/webinar/')