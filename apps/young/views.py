from django.shortcuts import render, redirect
from .models import Young, Fol, Met, Pic, Gal

def Youngviews(request):
    young = Young.objects.all()  
    fol = Fol.objects.all()
    met = Met.objects.all()
    pic = Pic.objects.all()
    gal = Gal.objects.all()

    context = {
        'young': young,
        'fol': fol,
        'met': met,
        'pic': pic,
        'gal': gal,
    }

    return render(request, 'young.html', context)

def lan_switch_young(request, lan):
    return redirect(f'/{lan}/young/')