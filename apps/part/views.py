from django.shortcuts import render, redirect
from .models import Part

def Partviews(request):
    part = Part.objects.all()  

    context = {
        'part': part,
    }

    return render(request, 'part.html', context)

def lan_switch_part(request, lan):
    return redirect(f'/{lan}/part/')
