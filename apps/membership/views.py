from django.shortcuts import render, redirect
from .models import Membership, Text, Image, Board

def Membershipviews(request):
    membership = Membership.objects.all() 
    text = Text.objects.all()
    image = Image.objects.all()
    board = Board.objects.all() 

    context = {
        'membership': membership,
        'text': text,
        'image': image,
        'board': board,
    }

    return render(request, 'membership.html', context)

def lan_switch_membership(request, lan):
    return redirect(f'/{lan}/membership/')
