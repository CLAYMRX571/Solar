from django.shortcuts import render, redirect
from .models import Award

def Awardviews(request):
    award = Award.objects.all()  

    context = {
        'award': award,
    }

    return render(request, 'award.html', context)

def lan_switch_award(request, lan):
    return redirect(f'/{lan}/award/')