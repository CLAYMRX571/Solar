from django.shortcuts import render, redirect
from .models import Eurosun

def Eurosunviews(request):
    eurosun = Eurosun.objects.all()  

    context = {
        'eurosun': eurosun,
    }

    return render(request, 'eurosun.html', context)

def lan_switch_eurosun(request, lan):
    return redirect(f'/{lan}/eurosun/')