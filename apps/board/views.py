from django.shortcuts import render, redirect
from .models import Board

def Boardviews(request):
    board = Board.objects.all()  

    context = {
        'board': board,
    }

    return render(request, 'board.html', context)

def lan_switch_board(request, lan):
    return redirect(f'/{lan}/board/')