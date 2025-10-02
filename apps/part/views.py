from django.shortcuts import render, redirect
from .models import Part, Cards, Pord

def Partviews(request):
    part = Part.objects.all()  
    cards = Cards.objects.all()
    pord = Pord.objects.all()

    context = {
        'part': part,
        'cards': cards,
        'pord': pord,
    }

    return render(request, 'part.html', context)

def lan_switch_part(request, lan):
    return redirect(f'/{lan}/part/')
