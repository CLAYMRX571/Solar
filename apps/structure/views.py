from django.shortcuts import render, redirect
from .models import Structure, Column, Card

def Structureviews(request):
    structure = Structure.objects.all() 
    column = Column.objects.all()
    card = Card.objects.all() 

    context = {
        'structure': structure,
        'column': column,
        'card': card,
    }

    return render(request, 'structure.html', context)

def lan_switch_structure(request, lan):
    return redirect(f'/{lan}/structure/')