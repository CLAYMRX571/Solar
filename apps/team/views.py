from django.shortcuts import render, redirect
from .models import Team, Cd

def Teamviews(request):
    team = Team.objects.all()  
    cd = Cd.objects.all()

    context = {
        'team': team,
        'cd': cd,
    }

    return render(request, 'team.html', context)

def lan_switch_team(request, lan):
    return redirect(f'/{lan}/team/')