from django.shortcuts import render, redirect
from .models import History, Coll, Greed

def Historyviews(request):
    history = History.objects.all()
    coll = Coll.objects.all()
    greed = Greed.objects.all()  

    context = {
        'history': history,
        'coll': coll,
        'greed': greed,
    }

    return render(request, 'history.html', context)

def lan_switch_history(request, lan):
    return redirect(f'/{lan}/history/')
