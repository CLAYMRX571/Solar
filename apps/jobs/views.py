from django.shortcuts import render, redirect
from .models import Jobs, Abs, Res, Look, Offer, Apply, Info, Foot

def Jobsviews(request):
    jobs = Jobs.objects.all()  
    abs = Abs.objects.all()
    res = Res.objects.all()
    look = Look.objects.all()
    offer = Offer.objects.all()
    apply = Apply.objects.all()
    info = Info.objects.all()
    foot = Foot.objects.all()

    context = {
        'jobs': jobs,
        'abs': abs,
        'res': res,
        'look': look,
        'offer': offer,
        'apply': apply,
        'info': info,
        'foot': foot,
    }

    return render(request, 'jobs.html', context)

def lan_switch_jobs(request, lan):
    return redirect(f'/{lan}/jobs/')
