from django.shortcuts import render, redirect
from .models import Public

def Publicviews(request):
    public = Public.objects.all()  

    context = {
        'public': public,
    }

    return render(request, 'public.html', context)

def lan_switch_public(request, lan):
    return redirect(f'/{lan}/public/')
