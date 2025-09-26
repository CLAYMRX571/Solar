from django.shortcuts import render, redirect
from .models import History

def Historyviews(request):
    history = History.objects.all()  

    context = {
        'history': history,
    }

    return render(request, 'history.html', context)

def lan_switch_history(request, lan):
    return redirect(f'/{lan}/history/')
