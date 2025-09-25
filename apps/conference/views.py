from django.shortcuts import render, redirect
from .models import Conference

def Conferenceviews(request):
    conference = Conference.objects.all()  

    context = {
        'conference': conference,
    }

    return render(request, 'conference.html', context)

def lan_switch_conference(request, lan):
    return redirect(f'/{lan}/conference/')