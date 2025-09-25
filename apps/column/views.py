from django.shortcuts import render, redirect
from .models import Column

def Columnviews(request):
    column = Column.objects.all()  

    context = {
        'column': column,
    }

    return render(request, 'column.html', context)

def lan_switch_column(request, lan):
    return redirect(f'/{lan}/column/')