from django.shortcuts import render, redirect
from .models import Incore, Core, Tess

def Incoreviews(request):
    incore = Incore.objects.all()
    core = Core.objects.all()
    tess = Tess.objects.all()

    context = {
        'incore': incore,
        'core': core,
        'tess': tess,
    }

    return render(request, 'incore.html', context)

def lan_switch_incore(request, lan):
    return redirect(f'/{lan}/incore/')