from django.shortcuts import render, redirect
from .models import Public, Pub

def Publicviews(request):
    public = Public.objects.all()  
    pub = Pub.objects.all()

    context = {
        'public': public,
        'pub': pub,
    }

    return render(request, 'public.html', context)

def lan_switch_public(request, lan):
    return redirect(f'/{lan}/public/')
