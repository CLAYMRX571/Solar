from django.shortcuts import render, redirect
from .models import Challenge

def Challengeviews(request):
    challenge = Challenge.objects.all()  

    context = {
        'challenge': challenge,
    }

    return render(request, 'challenge.html', context)

def lan_switch_challenge(request, lan):
    return redirect(f'/{lan}/challenge/')