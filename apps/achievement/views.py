from django.shortcuts import render, redirect
from .models import Achievement

def Achievementviews(request):
    achievement = Achievement.objects.all()  

    context = {
        'achievement': achievement,
    }

    return render(request, 'achievement.html', context)

def lan_switch_achievement(request, lan):
    return redirect(f'/{lan}/achievement/')