from django.shortcuts import render, redirect
from .models import Support

def Supportviews(request):
    support = Support.objects.all()  

    context = {
        'support': support,
    }

    return render(request, 'support.html', context)

def lan_switch_support(request, lan):
    return redirect(f'/{lan}/support/')