from django.shortcuts import render, redirect
from .models import Achievement

def Achievementviews(request):
    achivement = Achievement.objects.all()  

    context = {
        'achivement': achivement,
    }

    return render(request, 'achivement.html', context)

def lan_switch_achivement(request, lan):
    return redirect(f'/{lan}/achivement/')