from django.shortcuts import render, redirect
from .models import Journal

def Journalviews(request):
    journal = Journal.objects.all()  

    context = {
        'journal': journal,
    }

    return render(request, 'journal.html', context)

def lan_switch_journal(request, lan):
    return redirect(f'/{lan}/journal/')
