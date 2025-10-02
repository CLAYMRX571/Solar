from django.shortcuts import render, redirect
from .models import About, Key

def Aboutviews(request):
    about = About.objects.all()  
    key = Key.objects.all()

    context = {
        'about': about,
        'key': key,
    }

    return render(request, 'about.html', context)

def lan_switch_about(request, lan):
    return redirect(f'/{lan}/about/')
