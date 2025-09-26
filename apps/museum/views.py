from django.shortcuts import render, redirect
from .models import Museum

def Museumviews(request):
    museum = Museum.objects.all()  

    context = {
        'museum': museum,
    }

    return render(request, 'museum.html', context)

def lan_switch_museum(request, lan):
    return redirect(f'/{lan}/museum/')
