from django.shortcuts import render, redirect
from .models import Challenge, Galler, Anno, Wins

def Challengeviews(request):
    challenge = Challenge.objects.all() 
    galler = Galler.objects.all()
    anno = Anno.objects.all()
    wins = Wins.objects.all() 

    context = {
        'challenge': challenge,
        'galler': galler,
        'anno': anno,
        'wins': wins,
    }

    return render(request, 'challenge.html', context)

def lan_switch_challenge(request, lan):
    return redirect(f'/{lan}/challenge/')