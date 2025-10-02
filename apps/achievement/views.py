from django.shortcuts import render, redirect
from .models import Achievement, Recept, Past

def Achievementviews(request):
    achievement = Achievement.objects.all() 
    recept = Recept.objects.all() 
    past = Past.objects.all()

    context = {
        'achievement': achievement,
        'recept': recept,
        'past': past,
    }

    return render(request, 'achievement.html', context)

def lan_switch_achievement(request, lan):
    return redirect(f'/{lan}/achievement/')