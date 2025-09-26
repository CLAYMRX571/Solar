from django.shortcuts import render, redirect
from .models import Structure

def Structureviews(request):
    structure = Structure.objects.all()  

    context = {
        'structure': structure,
    }

    return render(request, 'structure.html', context)

def lan_switch_structure(request, lan):
    return redirect(f'/{lan}/structure/')