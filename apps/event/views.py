from django.shortcuts import render, redirect
from .models import Event, Text, Greeb

def Eventviews(request):
    event = Event.objects.all()  
    text = Text.objects.all()
    greeb = Greeb.objects.all()

    context = {
        'event': event,
        'text': text,
        'greeb': greeb,
    }

    return render(request, 'event.html', context)

def lan_switch_event(request, lan):
    return redirect(f'/{lan}/event/')