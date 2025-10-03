from django.shortcuts import render, redirect
from .models import Webinar, Bros, Bobs, Next, Crd

def Webinarviews(request):
    webinar = Webinar.objects.all()  
    bros = Bros.objects.all()
    bobs = Bobs.objects.all()
    next = Next.objects.all()
    crd = Crd.objects.all()

    context = {
        'webinar': webinar,
        'bros': bros,
        'bobs': bobs,
        'next': next,
        'crd': crd,
    }

    return render(request, 'webinar.html', context)

def lan_switch_webinar(request, lan):
    return redirect(f'/{lan}/webinar/')