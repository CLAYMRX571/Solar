from django.shortcuts import render, redirect
from .models import Advance

def Advanceviews(request):
    advance = Advance.objects.all()  

    context = {
        'advance': advance,
    }

    return render(request, 'advance.html', context)

def lan_switch_advance(request, lan):
    return redirect(f'/{lan}/advance/')