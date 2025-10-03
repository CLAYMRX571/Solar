from django.shortcuts import render, redirect
from .models import Journal, Table, Detail, Text 

def Journalviews(request):
    journal = Journal.objects.all()  
    table = Table.objects.all()
    detail = Detail.objects.all()
    text = Text.objects.all()

    context = {
        'journal': journal,
        'table': table,
        'detail': detail,
        'text': text,
    }

    return render(request, 'journal.html', context)

def lan_switch_journal(request, lan):
    return redirect(f'/{lan}/journal/')
