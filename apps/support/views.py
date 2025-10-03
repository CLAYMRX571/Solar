from django.shortcuts import render, redirect
from .models import Support, Miss, Invol

def Supportviews(request):
    support = Support.objects.all()  
    miss = Miss.objects.all()
    invol = Invol.objects.all()

    context = {
        'support': support,
        'miss': miss,
        'invol': invol,
    }

    return render(request, 'support.html', context)

def lan_switch_support(request, lan):
    return redirect(f'/{lan}/support/')