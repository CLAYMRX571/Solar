from django.shortcuts import render, redirect
from .models import Banner, Home, Latest

def Homeviews(request):
    banner = Banner.objects.all()
    home = Home.objects.all()
    latest = Latest.objects.all()

    context = {
        'banner': banner,
        'home': home,
        'latest': latest,
    }

    return render(request, 'index.html', context)

def lan_switch(request, lan):
    return redirect(f'/{lan}/')