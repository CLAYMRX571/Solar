from django.shortcuts import render, redirect
from .models import Eurosun, Conf, Sun

def Eurosunviews(request):
    eurosun = Eurosun.objects.all()  
    conf = Conf.objects.all()
    sun = Sun.objects.all()

    context = {
        'eurosun': eurosun,
        'conf': conf,
        'sun': sun,
    }

    return render(request, 'eurosun.html', context)

def lan_switch_eurosun(request, lan):
    return redirect(f'/{lan}/eurosun/')