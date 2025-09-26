from django.shortcuts import render, redirect
from .models import Young

def Youngviews(request):
    young = Young.objects.all()  

    context = {
        'young': young,
    }

    return render(request, 'young.html', context)

def lan_switch_young(request, lan):
    return redirect(f'/{lan}/young/')