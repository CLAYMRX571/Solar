from django.shortcuts import render, redirect
from .models import Event

def Eventviews(request):
    event = Event.objects.all()  

    context = {
        'event': event,
    }

    return render(request, 'event.html', context)

def lan_switch_event(request, lan):
    return redirect(f'/{lan}/event/')