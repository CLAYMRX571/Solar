from django.shortcuts import render, redirect
from .models import Banner, Home, Messages, Latest, Slide, Slides

def Homeviews(request):
    banner = Banner.objects.all()
    home = Home.objects.all()
    messages = Messages.objects.all()
    latest = Latest.objects.all()
    slide = Slide.objects.all()
    slides = Slides.objects.all()

    context = {
        'banner': banner,
        'home': home,
        'messages': messages,
        'latest': latest,
        'slide': slide,
        'slides': slides,
    }

    return render(request, 'index.html', context)

def lan_switch(request, lan):
    return redirect(f'/{lan}/')