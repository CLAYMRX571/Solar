from django.shortcuts import render, redirect
from .models import Incore

def Incoreviews(request):
    incore = Incore.objects.all()

    context = {
        'incore': incore,
    }

    return render(request, 'incore.html', context)

def lan_switch_incore(request, lan):
    return redirect(f'/{lan}/incore/')