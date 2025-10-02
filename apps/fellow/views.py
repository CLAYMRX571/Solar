from django.shortcuts import render, redirect
from .models import Fellow, Well, Lars, Gallery, Photo, Cent, Run

def Fellowviews(request):
    fellow = Fellow.objects.all()  
    well = Well.objects.all()
    lars = Lars.objects.all()
    gallery = Gallery.objects.all()
    photo = Photo.objects.all()
    cent = Cent.objects.all()
    run = Run.objects.all()

    context = {
        'fellow': fellow,
        'well': well,
        'lars': lars,
        'gallery': gallery,
        'photo': photo,
        'cent': cent,
        'run': run,
    }

    return render(request, 'fellow.html', context)

def lan_switch_fellow(request, lan):
    return redirect(f'/{lan}/fellow/')
