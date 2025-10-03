from django.shortcuts import render, redirect
from .models import Column, Data, Mons

def Columnviews(request):
    column = Column.objects.all()  
    data = Data.objects.all()
    mons = Mons.objects.all()

    context = {
        'column': column,
        'data': data,
        'mons': mons,
    }

    return render(request, 'column.html', context)

def lan_switch_column(request, lan):
    return redirect(f'/{lan}/column/')