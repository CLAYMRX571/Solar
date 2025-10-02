from django.shortcuts import render, redirect
from .models import Board, Ses, Member, Bar, Car

def Boardviews(request):
    board = Board.objects.all()  
    ses = Ses.objects.all()
    member = Member.objects.all()
    bar = Bar.objects.all()
    car = Car.objects.all()

    context = {
        'board': board,
        'ses': ses,
        'member': member,
        'bar': bar,
        'car': car,
    }

    return render(request, 'board.html', context)

def lan_switch_board(request, lan):
    return redirect(f'/{lan}/board/')