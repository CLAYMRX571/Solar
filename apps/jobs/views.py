from django.shortcuts import render, redirect
from .models import Jobs

def Jobsviews(request):
    jobs = Jobs.objects.all()  

    context = {
        'jobs': jobs,
    }

    return render(request, 'jobs.html', context)

def lan_switch_jobs(request, lan):
    return redirect(f'/{lan}/jobs/')
