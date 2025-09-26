from django.shortcuts import render, redirect
from .models import Daniel

def Danielviews(request):
    daniel = Daniel.objects.all()  

    context = {
        'daniel': daniel,
    }

    return render(request, 'daniel.html', context)

def lan_switch_daniel(request, lan):
    return redirect(f'/{lan}/daniel/')