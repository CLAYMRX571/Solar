from django.shortcuts import render, redirect
from .models import Leader

def Leaderviews(request):
    leader = Leader.objects.all()

    context = {
        'leader': leader,
    }

    return render(request, 'leader.html', context)

def lan_switch_leader(request, lan):
    return redirect(f'/{lan}/leader/')