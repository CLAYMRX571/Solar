from django.shortcuts import render, redirect
from .models import Leader, Cont, Win

def Leaderviews(request):
    leader = Leader.objects.all()
    cont = Cont.objects.all()
    win = Win.objects.all()

    context = {
        'leader': leader,
        'cont': cont,
        'win': win,
    }

    return render(request, 'leader.html', context)

def lan_switch_leader(request, lan):
    return redirect(f'/{lan}/leader/')