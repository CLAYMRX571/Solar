from django.shortcuts import render, redirect
from .models import Fellow

def Fellowviews(request):
    fellow = Fellow.objects.all()  

    context = {
        'fellow': fellow,
    }

    return render(request, 'fellow.html', context)

def lan_switch_fellow(request, lan):
    return redirect(f'/{lan}/fellow/')
