from django.shortcuts import render, redirect
from .models import Award, Link

def Awardviews(request):
    award = Award.objects.all()  
    link = Link.objects.all()

    context = {
        'award': award,
        'link': link,
    }

    return render(request, 'award.html', context)

def lan_switch_award(request, lan):
    return redirect(f'/{lan}/award/')