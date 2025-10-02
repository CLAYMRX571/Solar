from django.shortcuts import render, redirect
from .models import Daniel, Recep

def Danielviews(request):
    daniel = Daniel.objects.all() 
    recep = Recep.objects.all() 

    context = {
        'daniel': daniel,
        'recep': recep,
    }

    return render(request, 'daniel.html', context)

def lan_switch_daniel(request, lan):
    return redirect(f'/{lan}/daniel/')